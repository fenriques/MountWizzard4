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
import os
import json
# external packages
import PyQt5.QtCore
from mountcontrol import qtmount
# local import
import mainW
import messageW
import hemisphereW
from relay import kmRelay
from build import build


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

    def __init__(self,
                 mwGlob={},
                 splash=None,
                 ):
        super().__init__()

        self.mwGlob = mwGlob
        # persistence management through dict
        self.config = {}
        # todo: how to handle the splash screen ?
        if splash is not None:
            splash.showMessage('Load configuration')
            splash.setValue(65)
        self.loadConfig()

        # get the working horses up
        if splash is not None:
            splash.showMessage('Load mount')
            splash.setValue(70)

        pathToTs = self.mwGlob['configDir']
        self.mount = qtmount.Mount(host='192.168.2.15',
                                   MAC='00.c0.08.87.35.db',
                                   pathToTS=pathToTs,
                                   expire=False,
                                   verbose=False,
                                   )
        # relay box
        if splash is not None:
            splash.showMessage('Load relay')
            splash.setValue(75)
        self.relay = kmRelay.KMRelay(host='192.168.2.15',
                                     )

        # managing data
        self.mount.signals.mountUp.connect(self.loadMountData)

        # get the window widgets up
        if splash is not None:
            splash.showMessage('Load main widget')
            splash.setValue(80)
        self.data = build.DataPoint()
        self.mainW = mainW.MainWindow(self)
        if splash is not None:
            splash.showMessage('Load hemisphere widget')
            splash.setValue(90)
        self.hemisphereW = hemisphereW.HemisphereWindow(self)
        if splash is not None:
            splash.showMessage('Load message widget')
            splash.setValue(85)
        self.messageW = messageW.MessageWindow(self)

        # link cross widget gui signals
        self.mainW.ui.openMessageW.clicked.connect(self.messageW.toggleWindow)
        self.mainW.ui.openHemisphereW.clicked.connect(self.hemisphereW.toggleWindow)

        # starting cyclic polling of mount data
        self.mount.startTimers()

        # write basic data to message window
        self.message.emit('MountWizzard4 started', 1)
        self.message.emit('Workdir is: {0}'.format(self.mwGlob['workDir']), 1)

    def quit(self):
        """
        quit without saving persistence data

        :return:    nothing
        """

        self.mount.stopTimers()
        PyQt5.QtCore.QCoreApplication.quit()

    def quitSave(self):
        """
        quit with saving persistence data

        :param  name: name of configuration
        :return:    nothing
        """

        self.mount.stopTimers()
        self.mainW.storeConfig()
        self.messageW.storeConfig()
        self.hemisphereW.storeConfig()
        self.saveConfig()
        PyQt5.QtCore.QCoreApplication.quit()

    def loadConfig(self, filePath=None):
        """
        loadConfig loads a json file from disk and stores it to the config dicts for
        persistent data.

        :param      filePath:   full path to the config file
        :return:    success
        """

        if filePath is None:
            filePath = self.mwGlob['configDir'] + '/config.cfg'
        if not os.path.isfile(filePath):
            # new config necessary
            self.config = {'name': 'config',
                           'filePath': None,
                           'version': '4.0',
                           }
            return False
        # now try to read existing config
        try:
            with open(filePath, 'r') as data_file:
                loadData = json.load(data_file)
        except Exception as e:
            self.logger.error('Cannot parse: {0}, error: {1}'.format(filePath, e))
            return False
        filePath = loadData.get('filePath', None)
        if filePath is None:
            return False
        # config has reference to profile file
        if not os.path.isfile(filePath):
            # link is broken, we use the standard config data
            self.config = loadData
            return False
        try:
            with open(filePath, 'r') as data_file:
                loadData = json.load(data_file)
        except Exception as e:
            self.logger.error('Cannot parse: {0}, error: {1}'.format(filePath, e))
            # file is broken, we use the standard config data
            self.config = loadData
            return False
        if 'version' not in loadData:
            # data is missing, we use the standard config data
            self.config = loadData
            return False
        if loadData['version'] != '4.0':
            loadData = self.convertData(loadData)
        self.config = loadData
        return True

    def saveConfig(self, filePath=None, name='config'):
        """
        saveConfig saves a json file to disk from the config dicts for
        persistent data.

        :param      filePath:   full path to the config file
        :param      name:       name of the configuration
        :return:    success
        """

        # check necessary data available
        if filePath is None:
            filePath = self.mwGlob['configDir'] + '/' + name + '.cfg'
        self.config['filePath'] = filePath
        self.config['name'] = name
        # save the config
        configPath = self.mwGlob['configDir'] + '/' + 'config.cfg'
        with open(configPath, 'w') as outfile:
            json.dump(self.config,
                      outfile,
                      sort_keys=True,
                      indent=4)
        # there is a link to another config file, so we save it too
        if filePath is None:
            return False
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

        :param      status: connection status to mount computer
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
