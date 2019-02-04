# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'measure.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MeasureDialog(object):
    def setupUi(self, MeasureDialog):
        MeasureDialog.setObjectName("MeasureDialog")
        MeasureDialog.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MeasureDialog.sizePolicy().hasHeightForWidth())
        MeasureDialog.setSizePolicy(sizePolicy)
        MeasureDialog.setMinimumSize(QtCore.QSize(800, 600))
        MeasureDialog.setMaximumSize(QtCore.QSize(1600, 1200))
        MeasureDialog.setSizeIncrement(QtCore.QSize(10, 10))
        MeasureDialog.setBaseSize(QtCore.QSize(10, 10))
        font = QtGui.QFont()
        font.setFamily("Arial")
        MeasureDialog.setFont(font)
        self.measure = QtWidgets.QWidget(MeasureDialog)
        self.measure.setEnabled(True)
        self.measure.setGeometry(QtCore.QRect(5, 64, 790, 531))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.measure.sizePolicy().hasHeightForWidth())
        self.measure.setSizePolicy(sizePolicy)
        self.measure.setMinimumSize(QtCore.QSize(790, 270))
        self.measure.setMaximumSize(QtCore.QSize(1580, 1070))
        self.measure.setSizeIncrement(QtCore.QSize(10, 10))
        self.measure.setBaseSize(QtCore.QSize(10, 10))
        self.measure.setAutoFillBackground(True)
        self.measure.setStyleSheet("")
        self.measure.setObjectName("measure")
        self.tp0 = QtWidgets.QPushButton(MeasureDialog)
        self.tp0.setGeometry(QtCore.QRect(410, 30, 51, 23))
        self.tp0.setObjectName("tp0")
        self.tp1 = QtWidgets.QPushButton(MeasureDialog)
        self.tp1.setGeometry(QtCore.QRect(465, 30, 51, 23))
        self.tp1.setObjectName("tp1")
        self.tp2 = QtWidgets.QPushButton(MeasureDialog)
        self.tp2.setGeometry(QtCore.QRect(520, 30, 51, 23))
        self.tp2.setObjectName("tp2")
        self.tp3 = QtWidgets.QPushButton(MeasureDialog)
        self.tp3.setGeometry(QtCore.QRect(575, 30, 51, 23))
        self.tp3.setObjectName("tp3")
        self.tp4 = QtWidgets.QPushButton(MeasureDialog)
        self.tp4.setGeometry(QtCore.QRect(630, 30, 51, 23))
        self.tp4.setObjectName("tp4")
        self.tp5 = QtWidgets.QPushButton(MeasureDialog)
        self.tp5.setGeometry(QtCore.QRect(685, 30, 51, 23))
        self.tp5.setObjectName("tp5")
        self.ms0 = QtWidgets.QPushButton(MeasureDialog)
        self.ms0.setGeometry(QtCore.QRect(10, 30, 116, 23))
        self.ms0.setObjectName("ms0")
        self.ms1 = QtWidgets.QPushButton(MeasureDialog)
        self.ms1.setGeometry(QtCore.QRect(130, 30, 116, 23))
        self.ms1.setObjectName("ms1")
        self.label_110 = QtWidgets.QLabel(MeasureDialog)
        self.label_110.setGeometry(QtCore.QRect(410, 5, 156, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_110.setFont(font)
        self.label_110.setObjectName("label_110")
        self.line_32 = QtWidgets.QFrame(MeasureDialog)
        self.line_32.setGeometry(QtCore.QRect(410, 25, 381, 1))
        self.line_32.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_32.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_32.setObjectName("line_32")
        self.label_111 = QtWidgets.QLabel(MeasureDialog)
        self.label_111.setGeometry(QtCore.QRect(10, 5, 156, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_111.setFont(font)
        self.label_111.setObjectName("label_111")
        self.line_33 = QtWidgets.QFrame(MeasureDialog)
        self.line_33.setGeometry(QtCore.QRect(10, 25, 356, 1))
        self.line_33.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_33.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_33.setObjectName("line_33")
        self.ms2 = QtWidgets.QPushButton(MeasureDialog)
        self.ms2.setGeometry(QtCore.QRect(250, 30, 116, 23))
        self.ms2.setObjectName("ms2")
        self.tp6 = QtWidgets.QPushButton(MeasureDialog)
        self.tp6.setGeometry(QtCore.QRect(740, 30, 51, 23))
        self.tp6.setObjectName("tp6")

        self.retranslateUi(MeasureDialog)
        QtCore.QMetaObject.connectSlotsByName(MeasureDialog)

    def retranslateUi(self, MeasureDialog):
        _translate = QtCore.QCoreApplication.translate
        MeasureDialog.setWindowTitle(_translate("MeasureDialog", "Measurements"))
        self.tp0.setText(_translate("MeasureDialog", "3 Min"))
        self.tp1.setText(_translate("MeasureDialog", "10 Min"))
        self.tp2.setText(_translate("MeasureDialog", "30 Min"))
        self.tp3.setText(_translate("MeasureDialog", "1 Hr"))
        self.tp4.setText(_translate("MeasureDialog", "3 Hrs"))
        self.tp5.setText(_translate("MeasureDialog", "10 Hrs"))
        self.ms0.setText(_translate("MeasureDialog", "RaDec Stability"))
        self.ms1.setText(_translate("MeasureDialog", "Environment"))
        self.label_110.setText(_translate("MeasureDialog", "Time Window"))
        self.label_111.setText(_translate("MeasureDialog", "Measurement Sets"))
        self.ms2.setText(_translate("MeasureDialog", "Sky Quality"))
        self.tp6.setText(_translate("MeasureDialog", "10 Hrs"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MeasureDialog = QtWidgets.QWidget()
    ui = Ui_MeasureDialog()
    ui.setupUi(MeasureDialog)
    MeasureDialog.show()
    sys.exit(app.exec_())

