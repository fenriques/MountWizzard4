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
#
# Michael Würtenberger
# (c) 2019
#
# Licence APL2.0
#
###########################################################
from invoke import task

# defining environment for ubuntu
clientUbuntu = 'astro-ubuntu.fritz.box'
userUbuntu = 'mw@' + clientUbuntu
workUbuntu = userUbuntu + ':/home/mw/mountwizzard4'

# same for windows10 with cmd.exe as shell
clientWindows = 'astro-windows.fritz.box'
userWindows = 'mw@' + clientWindows
workWindows = userWindows + ':/Users/mw/mountwizzard4'
buildWindows = userWindows + ':/Users/mw/MountWizzard'


@task
def clean_mountwizzard(c):
    print('clean mountwizzard')
    c.run('rm -rf .pytest_cache')
    c.run('rm -rf mw4.egg-info')
    c.run('find ./mw4 | grep -E "(__pycache__)" | xargs rm -rf')


@task
def clean_mountcontrol(c):
    print('clean mountcontrol')
    with c.cd('../mountcontrol'):
        c.run('rm -rf .pytest_cache')
        c.run('rm -rf mountcontrol.egg-info')
        c.run('find ./mountcontrol | grep -E "(__pycache__)" | xargs rm -rf')


@task
def clean_indibase(c):
    print('clean')
    with c.cd('../indibase'):
        c.run('rm -rf .pytest_cache')
        c.run('rm -rf indibase.egg-info')
        c.run('find ./indibase | grep -E "(__pycache__)" | xargs rm -rf')


@task
def resource(c):
    print('building resources')
    resourceDir = 'mw4/gui/media/'
    c.run(f'pyrcc5 -o {resourceDir}resources.py {resourceDir}resources.qrc')


@task
def widgets(c):
    print('building widgets')
    widgetDir = 'mw4/gui/widgets/'
    widgets = ['hemisphere', 'image', 'main', 'measure', 'message', 'satellite']
    for widget in widgets:
        name = widgetDir + widget
        c.run(f'python -m PyQt5.uic.pyuic -x {name}.ui -o {name}_ui.py')


@task()
def test_mountcontrol(c):
    print('testing mountcontrol')
    with c.cd('../mountcontrol'):
        c.run('flake8')
        c.run('pytest mountcontrol/test/test_units --cov-config .coveragerc --cov mountcontrol/')


@task()
def test_indibase(c):
    print('testing indibase')
    with c.cd('../indibase'):
        c.run('flake8')
        c.run('pytest indibase/test/test_units --cov-config .coveragerc --cov mw4/')


@task(pre=[resource, widgets])
def test_mountwizzard(c):
    print('testing mountwizzard')
    c.run('flake8')
    c.run('pytest mw4/test/test_units --cov-config .coveragerc --cov mw4/')


@task(pre=[test_mountcontrol, clean_mountcontrol])
def build_mountcontrol(c):
    print('building dist mountcontrol')
    with c.cd('../mountcontrol'):
        c.run('rm -f dist/*.tar.gz')
        c.run('python setup.py sdist bdist_egg')


@task(pre=[])
def build_indibase(c):
    print('building dist indibase')
    with c.cd('../indibase'):
        c.run('rm -f dist/*.tar.gz')
        c.run('python setup.py sdist')


@task(pre=[build_mountcontrol, build_indibase])
def build_dist(c):
    print('building dist mountwizzard4')
    c.run('rm -f dist/*.tar.gz')
    c.run('python setup.py sdist')


@task()
def venv_linux(c):
    print('preparing linux')
    with c.cd('remote_scripts'):
        c.run(f'ssh -t {userUbuntu} "bash -s" < setup_linux.sh')


@task()
def venv_windows(c):
    print('preparing windows')
    with c.cd('remote_scripts'):
        c.run(f'ssh {userWindows} < setup_windows.bat')


@task()
def venv_mac(c):
    print('preparing maac')
    with c.cd('remote_scripts'):
        pass


@task(pre=[venv_windows, build_dist])
def build_windows_app(c):
    print('build windows app and exe')
    c.run(f'ssh {userWindows} "if exist MountWizzard (rmdir /s/q MountWizzard)"')
    c.run(f'ssh {userWindows} "mkdir MountWizzard"')
    with c.cd('../mountcontrol'):
        c.run(f'scp dist/*.tar.gz {buildWindows}/mc.tar.gz')
    with c.cd('../indibase'):
        c.run(f'scp dist/*.tar.gz {buildWindows}/ib.tar.gz')
    c.run(f'scp dist/*.tar.gz {buildWindows}/mw4.tar.gz')
    c.run(f'scp mw4_windows_debug.spec {buildWindows}')
    with c.cd('remote_scripts'):
        c.run(f'scp mw4.ico {buildWindows}')
    with c.cd('remote_scripts'):
        c.run(f'ssh {userWindows} < build_windows.bat')
    c.run(f'scp {buildWindows}/dist/MountWizzard4-console.exe ./dist/')


@task(pre=[venv_mac, build_dist])
def build_mac_app(c):
    print('building mac app and dmg')
    print('update mountcontrol')
    c.run('pip install ../mountcontrol/dist/mountcontrol-*.tar.gz')
    print('update indibase')
    c.run('pip install ../indibase/dist/indibase-*.tar.gz')
    print('pyinstaller')
    c.run('pyinstaller -y mw4_mac.spec')
    print('building dmg')
    c.run('hdiutil create dist/MountWizzard4.dmg -srcfolder dist/*.app -ov')


@task(pre=[venv_linux])
def deploy_ubuntu(c):
    print('deploy ubuntu for test')
    c.run(f'ssh {userUbuntu} "bash -s" rm -rf mountwizzard4')
    c.run(f'ssh {userUbuntu} "bash -s" mkdir mountwizzard4')
    with c.cd('../mountcontrol'):
        c.run(f'scp dist/*.tar.gz {workUbuntu}/mc.tar.gz')
    with c.cd('../indibase'):
        c.run(f'scp dist/*.tar.gz {workUbuntu}ib.tar.gz')
    c.run(f'scp dist/*.tar.gz {workUbuntu}/mw4.tar.gz')
    with c.cd('remote_scripts'):
        c.run(f'scp start_ubuntu.sh {workUbuntu}')
        c.run(f'ssh {userUbuntu} "bash -s" < install_dist_ubuntu.sh')


@task(pre=[venv_windows, build_dist])
def deploy_windows_dist(c):
    print('deploy windows dist for test')
    c.run(f'ssh {userWindows} "if exist mountwizzard4 (rmdir /s/q mountwizzard4)"')
    c.run(f'ssh {userWindows} "mkdir mountwizzard4"')
    with c.cd('../mountcontrol'):
        c.run(f'scp dist/*.tar.gz {workWindows}/mc.tar.gz')
    with c.cd('../indibase'):
        c.run(f'scp dist/*.tar.gz {workWindows}/ib.tar.gz')
    c.run(f'scp dist/*.tar.gz {workWindows}/mw4.tar.gz')
    with c.cd('remote_scripts'):
        c.run(f'scp start_windows.bat {workWindows}')
        c.run(f'ssh {userWindows} < install_dist_windows.bat')


@task(pre=[build_windows_app])
def deploy_windows_app(c):
    print('deploy windows console.exe for test')
    c.run(f'ssh {userWindows} "if exist mountwizzard4 (rmdir /s/q mountwizzard4)"')
    c.run(f'ssh {userWindows} "mkdir mountwizzard4"')
    with c.cd('./dist'):
        c.run(f'scp MountWizzard4-console.exe {workWindows}')
    with c.cd('remote_scripts'):
        c.run(f'ssh {userWindows} < start_windows_app.bat')


@task(pre=[build_mac_app])
def deploy_mac_app(c):
    print('deploy mac for test')
    c.run('rm -rf /Users/mw/PycharmProjects/test')
    c.run('mkdir /Users/mw/PycharmProjects/test')
    c.run('cp -R dist/MountWizzard4.app /Users/mw/PycharmProjects/test')
    with c.cd('/Users/mw/PycharmProjects/test'):
        c.run('./MountWizzard4.app/Contents/MacOS/MountWizzard4 test')