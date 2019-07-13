# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mw4/gui/widgets/satellite.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SatelliteDialog(object):
    def setupUi(self, SatelliteDialog):
        SatelliteDialog.setObjectName("SatelliteDialog")
        SatelliteDialog.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SatelliteDialog.sizePolicy().hasHeightForWidth())
        SatelliteDialog.setSizePolicy(sizePolicy)
        SatelliteDialog.setMinimumSize(QtCore.QSize(800, 600))
        SatelliteDialog.setMaximumSize(QtCore.QSize(1600, 1200))
        SatelliteDialog.setSizeIncrement(QtCore.QSize(10, 10))
        SatelliteDialog.setBaseSize(QtCore.QSize(10, 10))
        font = QtGui.QFont()
        font.setFamily("Arial")
        SatelliteDialog.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(SatelliteDialog)
        self.verticalLayout.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(0, 0, -1, -1)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(SatelliteDialog)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.satSphere1 = QtWidgets.QWidget(SatelliteDialog)
        self.satSphere1.setObjectName("satSphere1")
        self.verticalLayout_2.addWidget(self.satSphere1)
        self.line = QtWidgets.QFrame(SatelliteDialog)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setMidLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.label_4 = QtWidgets.QLabel(SatelliteDialog)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.satSphere2 = QtWidgets.QWidget(SatelliteDialog)
        self.satSphere2.setObjectName("satSphere2")
        self.verticalLayout_2.addWidget(self.satSphere2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.line_3 = QtWidgets.QFrame(SatelliteDialog)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setMidLineWidth(1)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_3.addWidget(self.line_3)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(SatelliteDialog)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.satEarth = QtWidgets.QWidget(SatelliteDialog)
        self.satEarth.setObjectName("satEarth")
        self.verticalLayout_3.addWidget(self.satEarth)
        self.line_2 = QtWidgets.QFrame(SatelliteDialog)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setMidLineWidth(1)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_3.addWidget(self.line_2)
        self.label = QtWidgets.QLabel(SatelliteDialog)
        self.label.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.satHorizon = QtWidgets.QWidget(SatelliteDialog)
        self.satHorizon.setObjectName("satHorizon")
        self.verticalLayout_3.addWidget(self.satHorizon)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout.setStretch(0, 1)

        self.retranslateUi(SatelliteDialog)
        QtCore.QMetaObject.connectSlotsByName(SatelliteDialog)

    def retranslateUi(self, SatelliteDialog):
        _translate = QtCore.QCoreApplication.translate
        SatelliteDialog.setWindowTitle(_translate("SatelliteDialog", "Satellite"))
        self.label_3.setText(_translate("SatelliteDialog", "   Satellite orbit in relation to turning earth"))
        self.label_4.setText(_translate("SatelliteDialog", "   Satellite orbit in relation to fixed observer"))
        self.label_2.setText(_translate("SatelliteDialog", "   Satellite path over earth surface (subpoints)"))
        self.label.setText(_translate("SatelliteDialog", "   Satellite path over horizon from observers location"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SatelliteDialog = QtWidgets.QWidget()
    ui = Ui_SatelliteDialog()
    ui.setupUi(SatelliteDialog)
    SatelliteDialog.show()
    sys.exit(app.exec_())
