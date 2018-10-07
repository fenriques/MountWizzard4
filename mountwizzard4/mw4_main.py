############################################################
# -*- coding: utf-8 -*-
#
#       #   #  #   #   #    #
#      ##  ##  #  ##  #    #
#     # # # #  # # # #    #  #
#    #  ##  #  ##  ##    ######
#   #   #   #  #   #       #
#
# Python-based Tool for interaction with the 10micron mounts
# GUI with PyQT5 for python
# Python  v3.6.5
#
# Michael Würtenberger
# (c) 2018
#
# Licence APL2.0
#
###########################################################
# standard libraries
import logging
# external packages
import PyQt5.QtCore
# local import
import mw4_global
import mountcontrol.qtmount
import gui.mainW
import gui.messageW


class MountWizzard4(PyQt5.QtCore.QObject):
    """
    MountWizzard4 class is the main class for the application. it loads all windows and
    classes needed to fulfil the work of mountwizzard. any gui work should be handled
    through the window classes. main class is for setup, config, start, persist and
    shutdown the application.
    """

    __all__ = ['MountWizzard4',
               ]
    version = '0.1'
    logger = logging.getLogger(__name__)

    # central message and logging dispatching
    message = PyQt5.QtCore.pyqtSignal(str, int)

    def __init__(self):
        super().__init__()

        # persistence management through dict
        self.config = {}

        # get the working horses up
        pathToTs = mw4_global.work_dir + '/config'
        self.mount = mountcontrol.qtmount.Mount(host='192.168.2.15',
                                                MAC='00.c0.08.87.35.db',
                                                pathToTS=pathToTs,
                                                expire=False,
                                                verbose=False,
                                                )
        # managing data
        self.mount.signals.mountUp.connect(self.loadMountData)

        # get the window widgets up
        self.mainW = gui.mainW.MainWindow(self)
        self.messageW = gui.messageW.MessageWindow(self)

        # starting cyclic polling of mount data
        self.mount.startTimers()

        # write basic data to message window
        self.message.emit('MountWizzard4 started', 1)
        self.message.emit('Workdir is: {0}\n'.format(mw4_global.work_dir), 0)

    def quit(self):
        """
        quit without saving persistence data

        :return:    nothing
        """

        self.mount.stopTimers()
        PyQt5.QtCore.QCoreApplication.quit()

    def loadConfig(self, filePath, name):
        """
        loadConfig loads a json file from disk and stores it to the config dicts for
        persistent data.

        :param      filePath:   full path to the config file
        :param      name:       name of the config file
        :return:    success
        """

        if not os.path.isfile(filePath):
            return False
        with open(filePath, 'r') as data_file:
            loadData = json.load(data_file)
        if 'version' not in loadData:
            return False
        if 'name' not in loadData:
            return False
        if loadData['name'] != name:
            return
        if loadData['version'] != '4.0':
            loadData = self.convertData(loadData)
        self.config = loadData
        return True

    def saveConfig(self, filePath, name):
        """
        saveConfig saves a json file to disk from the config dicts for
        persistent data.

        :param      filePath:   full path to the config file
        :param      name:       name of the config file
        :return:    success
        """

        self.config['version'] = '4.0'
        self.config['name'] = name

        with open(filePath, 'w') as outfile:
            # make the file human readable
            json.dump(self.config,
                      outfile,
                      sort_keys=True,
                      indent=4)
        return True

    def convertData(self, data):
        """
        convertDate tries to convert data from an older or newer version of the config
        file to the actual needed one.

        :param      data:   config data as dict
        :return:    data:   config data as dict
        """
        return data

    def loadMountData(self, status):
        """
        loadMountData polls data from mount if connected otherwise clears all entries
        in attributes.

        :param      status: connection status to moutn computer
        :return:    True if success for test
        """
        if status:
            self.mount.workaround()
            self.mount.getFW()
            self.mount.getLocation()
            self.mount.cycleSetting()
            self.mount.getNames()
            self.mount.getAlign()
        else:
            self.mount.resetData()
        return True
