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
# Python  v3.7.5
#
# Michael Würtenberger
# (c) 2019
#
# Licence APL2.0
#
###########################################################
# standard libraries
import unittest.mock as mock
import pytest
# external packages
import PyQt5.QtGui
import PyQt5.QtWidgets
import PyQt5.uic
import PyQt5.QtTest
import PyQt5.QtCore
# local import
from mw4.test.test_units.setupQt import setupQt


@pytest.fixture(autouse=True, scope='module')
def module_setup_teardown():
    global app, spy, mwGlob, test
    app, spy, mwGlob, test = setupQt()
    yield


def test_initConfig_1():
    app.config['mainW'] = {}
    app.mainW.initConfig()
    assert app.mainW.ui.targetRMS.value() == 99
    assert not app.mainW.ui.checkShowErrorValues.isChecked()


def test_storeConfig_1():
    app.mainW.ui.targetRMS.setValue(33)
    app.mainW.ui.checkShowErrorValues.setChecked(True)
    app.mainW.storeConfig()
    conf = app.config['mainW']
    assert conf['checkShowErrorValues']
    assert 33 == conf['targetRMS']


def test_setupIcons():
    assert app.mainW.setupIcons()


def test_setNameList():
    value = ['Test1', 'test2', 'test3', 'test4']
    app.mount.model.nameList = value
    app.mainW.setNameList(app.mount.model)
    assert 4 == app.mainW.ui.nameList.count()
    value = None
    app.mount.model.nameList = value
    app.mainW.setNameList(app.mount.model)
    assert 0 == app.mainW.ui.nameList.count()


def test_showModelPolar1():
    app.mount.obsSite.location = ['49:00:00', '11:00:00', '580']
    app.mount.model.parseStars(['21:52:58.95,+08*56:10.1,   5.7,201',
                                '21:06:10.79,+45*20:52.8,  12.1,329',
                                '23:13:58.02,+38*48:18.8,  31.0,162',
                                '17:43:41.26,+59*15:30.7,   8.4,005',
                                ],
                               4)
    app.mainW.ui.checkShowErrorValues.setChecked(True)
    suc = app.mainW.showModelPolar(app.mount.model)
    assert suc


def test_showModelPolar2():
    app.mount.obsSite.location = ['49:00:00', '11:00:00', '580']
    app.mount.model._starList = list()
    app.mainW.ui.checkShowErrorValues.setChecked(True)
    suc = app.mainW.showModelPolar(app.mount.model)
    assert not suc


def test_showModelPolar3():
    app.mount.obsSite.location = []
    app.mount.model._starList = list()
    app.mainW.ui.checkShowErrorValues.setChecked(True)
    suc = app.mainW.showModelPolar(app.mount.model)
    assert not suc


def test_showModelPolar4():
    app.mainW.ui.checkShowErrorValues.setChecked(True)
    app.mount.model._starList = list()
    suc = app.mainW.showModelPolar(app.mount.model)
    assert not suc


def test_clearRefreshName():
    app.mount.signals.namesDone.connect(app.mainW.clearRefreshName)
    suc = app.mainW.clearRefreshName()
    assert suc


def test_refreshName_1():
    with mock.patch.object(app.mount,
                           'getNames',
                           return_value=True):
        suc = app.mainW.refreshName()
        assert suc
        suc = app.mainW.clearRefreshName()
        assert suc


def test_refreshName_2(qtbot):
    suc = app.mainW.refreshName()
    assert suc
    with qtbot.waitSignal(app.message) as blocker:
        suc = app.mainW.refreshName()
        assert suc
        assert ['Model names refreshed', 0] == blocker.args


def test_loadName_1(qtbot):
    with mock.patch.object(app.mainW.ui.nameList,
                           'currentItem',
                           return_value=None):
        with qtbot.waitSignal(app.message) as blocker:
            suc = app.mainW.loadName()
            assert not suc
            assert ['No model name selected', 2] == blocker.args


def test_loadName_2(qtbot):
    class Test:
        pass

        @staticmethod
        def text():
            return 'test'
    with mock.patch.object(app.mainW.ui.nameList,
                           'currentItem',
                           return_value=Test):
        with mock.patch.object(app.mount.model,
                               'loadName',
                               return_value=True):
            with qtbot.waitSignal(app.message) as blocker:
                suc = app.mainW.loadName()
                assert suc
                assert ['Model [test] loaded', 0] == blocker.args


def test_loadName_3(qtbot):
    class Test:
        pass

        @staticmethod
        def text():
            return 'test'
    with mock.patch.object(app.mainW.ui.nameList,
                           'currentItem',
                           return_value=Test):
        with mock.patch.object(app.mount.model,
                               'loadName',
                               return_value=False):
            with qtbot.waitSignal(app.message) as blocker:
                suc = app.mainW.loadName()
                assert not suc
                assert ['Model [test] cannot be loaded', 2] == blocker.args


def test_saveName_1(qtbot):
    with mock.patch.object(PyQt5.QtWidgets.QInputDialog,
                           'getText',
                           return_value=('', True)):
        with qtbot.waitSignal(app.message) as blocker:
            suc = app.mainW.saveName()
            assert not suc
            assert ['No model name given', 2] == blocker.args


def test_saveName_2(qtbot):
    with mock.patch.object(PyQt5.QtWidgets.QInputDialog,
                           'getText',
                           return_value=(None, True)):
        with qtbot.waitSignal(app.message) as blocker:
            suc = app.mainW.saveName()
            assert not suc
            assert ['No model name given', 2] == blocker.args


def test_saveName_3(qtbot):
    with mock.patch.object(PyQt5.QtWidgets.QInputDialog,
                           'getText',
                           return_value=('test', False)):
        with qtbot.assertNotEmitted(app.message):
            suc = app.mainW.saveName()
            assert not suc


def test_saveName_4(qtbot):
    with mock.patch.object(PyQt5.QtWidgets.QInputDialog,
                           'getText',
                           return_value=('test', True)):
        with mock.patch.object(app.mount.model,
                               'storeName',
                               return_value=False):
            with qtbot.waitSignal(app.message) as blocker:
                suc = app.mainW.saveName()
                assert not suc
                assert ['Model [test] cannot be saved', 2] == blocker.args


def test_saveName_5(qtbot):
    with mock.patch.object(PyQt5.QtWidgets.QInputDialog,
                           'getText',
                           return_value=('test', True)):
        with mock.patch.object(app.mount.model,
                               'storeName',
                               return_value=True):
            with qtbot.waitSignal(app.message) as blocker:
                suc = app.mainW.saveName()
                assert suc
                assert ['Model [test] saved', 0] == blocker.args


def test_deleteName_1(qtbot):
    with mock.patch.object(app.mainW.ui.nameList,
                           'currentItem',
                           return_value=None):
        with qtbot.waitSignal(app.message) as blocker:
            suc = app.mainW.deleteName()
            assert not suc
            assert ['No model name selected', 2] == blocker.args


def test_deleteName_2(qtbot):
    class Test:
        pass

        @staticmethod
        def text():
            return 'test'
    with mock.patch.object(app.mainW.ui.nameList,
                           'currentItem',
                           return_value=Test):
        with mock.patch.object(PyQt5.QtWidgets.QMessageBox,
                               'question',
                               return_value=PyQt5.QtWidgets.QMessageBox.No):
            with qtbot.assertNotEmitted(app.message):
                suc = app.mainW.deleteName()
                assert not suc


def test_deleteName_3(qtbot):
    class Test:
        pass

        @staticmethod
        def text():
            return 'test'
    with mock.patch.object(app.mainW.ui.nameList,
                           'currentItem',
                           return_value=Test):
        with mock.patch.object(PyQt5.QtWidgets.QMessageBox,
                               'question',
                               return_value=PyQt5.QtWidgets.QMessageBox.Yes):
            with mock.patch.object(app.mount.model,
                                   'deleteName',
                                   return_value=True):
                with qtbot.waitSignal(app.message) as blocker:
                    suc = app.mainW.deleteName()
                    assert suc
                    assert ['Model [test] deleted', 0] == blocker.args


def test_deleteName_4(qtbot):
    class Test:
        pass

        @staticmethod
        def text():
            return 'test'
    with mock.patch.object(app.mainW.ui.nameList,
                           'currentItem',
                           return_value=Test):
        with mock.patch.object(PyQt5.QtWidgets.QMessageBox,
                               'question',
                               return_value=PyQt5.QtWidgets.QMessageBox.Yes):
            with mock.patch.object(app.mount.model,
                                   'deleteName',
                                   return_value=False):
                with qtbot.waitSignal(app.message) as blocker:
                    suc = app.mainW.deleteName()
                    assert not suc
                    assert ['Model [test] cannot be deleted', 2] == blocker.args


def test_cancelTargetRMS():
    app.mainW.runningTargetRMS = True
    suc = app.mainW.cancelTargetRMS()
    assert suc
    assert not app.mainW.runningTargetRMS


def test_clearRefreshModel():
    app.mount.signals.alignDone.connect(app.mainW.clearRefreshModel)
    suc = app.mainW.clearRefreshModel()
    assert suc


def test_refreshModel():
    app.mount.signals.alignDone.connect(app.mainW.clearRefreshModel)
    with mock.patch.object(app.mount,
                           'getAlign'):
        suc = app.mainW.clearRefreshModel()
        assert suc


def test_clearRunTargetRMS_1():
    app.mount.signals.alignDone.connect(app.mainW.clearRunTargetRMS)
    app.mount.model.errorRMS = 0.1
    suc = app.mainW.clearRunTargetRMS()
    assert suc


def test_clearRunTargetRMS_2():
    app.mount.model.addStar('12:00:00, 180:00:00, 5, 90, 1')
    app.mount.model.addStar('12:00:00, 120:00:00, 4, 90, 2')
    app.mount.model.errorRMS = 100
    app.mainW.runningTargetRMS = True
    app.mount.signals.alignDone.connect(app.mainW.clearRunTargetRMS)
    with mock.patch.object(app.mount.model,
                           'deletePoint',
                           return_value=False):
        with mock.patch.object(app.mount,
                               'getAlign'):
            suc = app.mainW.clearRunTargetRMS()
            assert suc


def test_clearRunTargetRMS_3():
    app.mount.model.addStar('12:00:00, 180:00:00, 5, 90, 1')
    app.mount.model.addStar('12:00:00, 120:00:00, 4, 90, 2')
    app.mount.model.errorRMS = 100
    app.mainW.runningTargetRMS = True
    app.mount.signals.alignDone.connect(app.mainW.clearRunTargetRMS)
    with mock.patch.object(app.mount.model,
                           'deletePoint',
                           return_value=True):
        with mock.patch.object(app.mount,
                               'getAlign'):
            suc = app.mainW.clearRunTargetRMS()
            assert suc


def test_clearRunTargetRMS_4():
    app.mount.model.errorRMS = 100
    app.mainW.runningTargetRMS = False
    app.mount.signals.alignDone.connect(app.mainW.clearRunTargetRMS)
    suc = app.mainW.clearRunTargetRMS()
    assert suc


def test_runTargetRMS():
    with mock.patch.object(app.mainW,
                           'clearRunTargetRMS'):
        suc = app.mainW.runTargetRMS()
        assert suc
    app.mount.signals.alignDone.connect(app.mainW.clearRunTargetRMS)


def test_cancelTargetRMS():
    suc = app.mainW.cancelTargetRMS()
    assert suc
    assert not app.mainW.runningTargetRMS


def test_clearModel_1(qtbot):
    with mock.patch.object(PyQt5.QtWidgets.QMessageBox,
                           'question',
                           return_value=PyQt5.QtWidgets.QMessageBox.No):
        suc = app.mainW.clearModel()
        assert not suc


def test_clearModel_2(qtbot):
    with mock.patch.object(PyQt5.QtWidgets.QMessageBox,
                           'question',
                           return_value=PyQt5.QtWidgets.QMessageBox.Yes):
        with mock.patch.object(app.mount.model,
                               'clearAlign',
                               return_value=False):
            with qtbot.waitSignal(app.message) as blocker:
                suc = app.mainW.clearModel()
                assert not suc
                assert ['Actual model cannot be cleared', 2] == blocker.args


def test_clearModel_3(qtbot):
    with mock.patch.object(PyQt5.QtWidgets.QMessageBox,
                           'question',
                           return_value=PyQt5.QtWidgets.QMessageBox.Yes):
        with mock.patch.object(app.mount.model,
                               'clearAlign',
                               return_value=True):
            with qtbot.waitSignal(app.message) as blocker:
                suc = app.mainW.clearModel()
                assert suc
                assert ['Actual model cleared', 0] == blocker.args


def test_deleteWorstPoint_1():
    app.mount.model.addStar('12:00:00, 180:00:00, 5, 90, 1')
    app.mount.model.addStar('12:00:00, 120:00:00, 4, 90, 2')
    with mock.patch.object(app.mount.model,
                           'deletePoint',
                           return_value=False):
        suc = app.mainW.deleteWorstPoint()
        assert not suc


def test_deleteWorstPoint_2():
    app.mount.model.addStar('12:00:00, 180:00:00, 5, 90, 1')
    app.mount.model.addStar('12:00:00, 120:00:00, 4, 90, 2')
    with mock.patch.object(app.mount.model,
                           'deletePoint',
                           return_value=True):
        with mock.patch.object(app.mainW,
                               'refreshModel'):
            suc = app.mainW.deleteWorstPoint()
            assert suc
