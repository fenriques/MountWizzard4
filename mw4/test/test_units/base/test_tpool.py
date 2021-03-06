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
from unittest import mock
import time
import pytest
# external packages
# local import
from mw4.test.test_units.setupQt import setupQt
from mw4.base import tpool


@pytest.fixture(autouse=True, scope='module')
def module_setup_teardown():
    global app, spy, mwGlob, test, host
    app, spy, mwGlob, test = setupQt()
    host_ip = '192.168.2.250'
    host = (host_ip, 80)


def test_WorkerSignals():
    a = tpool.WorkerSignals()
    assert a.finished
    assert a.error
    assert a.result


def test_Worker_1():
    def testFunc():
        return 'test'
    a = tpool.Worker(testFunc)
    assert a.signals


def test_Worker_2(qtbot):
    def testFunc():
        return 'test'
    a = tpool.Worker(testFunc)

    with qtbot.waitSignal(a.signals.finished):
        a.run()


def test_Worker_3(qtbot):
    def testFunc():
        return 'test'
    a = tpool.Worker(testFunc)

    with qtbot.waitSignal(a.signals.result):
        a.run()


def test_Worker_4(qtbot):
    def testFunc():
        return 'test'
    a = tpool.Worker(testFunc)

    with qtbot.assertNotEmitted(a.signals.error):
        a.run()


def test_Worker_5(qtbot):
    def testFunc():
        raise Exception('Test')
        return 'test'
    a = tpool.Worker(testFunc)

    with qtbot.waitSignal(a.signals.error):
        a.run()
