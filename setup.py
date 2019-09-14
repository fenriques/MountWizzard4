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
from setuptools import setup

setup(
    name='mw4',
    version='0.112',
    packages=[
        'mw4',
        'mw4.astrometry',
        'mw4.base',
        'mw4.dome',
        'mw4.environment',
        'mw4.gui',
        'mw4.gui.media',
        'mw4.gui.widgets',
        'mw4.gui.mainWmixin',
        'mw4.imaging',
        'mw4.modeldata',
        'mw4.powerswitch',
        'mw4.remote',
    ],
    python_requires='>=3.7.2',
    install_requires=[
        'mountcontrol',
        'indibase',
        'PyQt5>=5.13',
        'matplotlib>=3.1.1',
        'astropy>=3.2.1',
        'requests>=2.22.0',
        'requests_toolbelt>=0.9.1',
        'numpy>=1.17',
        'skyfield>=1.10',
        'forwardable',
    ],
    url='https://github.com/mworion/MountWizzard4',
    license='APL 2.0',
    author='mworion',
    author_email='michael@wuertenberger.org',
    description='tooling for a 10micron mount',
    zip_safe=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming language .. Python .. 3.7',
        'Operating System :: OS Independent',
        'Topic :: Utilities',
        'License :: OSI Approved :: Apache Software License',
    ]
)
