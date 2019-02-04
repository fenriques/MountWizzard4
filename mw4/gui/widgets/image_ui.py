# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'image.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ImageDialog(object):
    def setupUi(self, ImageDialog):
        ImageDialog.setObjectName("ImageDialog")
        ImageDialog.resize(800, 600)
        ImageDialog.setMinimumSize(QtCore.QSize(800, 400))
        ImageDialog.setMaximumSize(QtCore.QSize(1600, 1200))
        font = QtGui.QFont()
        font.setFamily("Arial")
        ImageDialog.setFont(font)
        self.image = QtWidgets.QWidget(ImageDialog)
        self.image.setGeometry(QtCore.QRect(5, 125, 790, 470))
        self.image.setMinimumSize(QtCore.QSize(790, 270))
        self.image.setMaximumSize(QtCore.QSize(1580, 1070))
        self.image.setAutoFillBackground(True)
        self.image.setObjectName("image")
        self.expose = QtWidgets.QPushButton(ImageDialog)
        self.expose.setGeometry(QtCore.QRect(10, 15, 76, 26))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.expose.sizePolicy().hasHeightForWidth())
        self.expose.setSizePolicy(sizePolicy)
        self.expose.setMinimumSize(QtCore.QSize(76, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.expose.setFont(font)
        self.expose.setObjectName("expose")
        self.solve = QtWidgets.QPushButton(ImageDialog)
        self.solve.setGeometry(QtCore.QRect(170, 15, 76, 26))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.solve.setFont(font)
        self.solve.setObjectName("solve")
        self.load = QtWidgets.QPushButton(ImageDialog)
        self.load.setEnabled(True)
        self.load.setGeometry(QtCore.QRect(10, 45, 76, 26))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.load.setFont(font)
        self.load.setObjectName("load")
        self.cancel = QtWidgets.QPushButton(ImageDialog)
        self.cancel.setGeometry(QtCore.QRect(250, 15, 76, 26))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cancel.setFont(font)
        self.cancel.setObjectName("cancel")
        self.imageFileName = QtWidgets.QLineEdit(ImageDialog)
        self.imageFileName.setEnabled(False)
        self.imageFileName.setGeometry(QtCore.QRect(90, 45, 236, 26))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.imageFileName.setFont(font)
        self.imageFileName.setMouseTracking(False)
        self.imageFileName.setFocusPolicy(QtCore.Qt.NoFocus)
        self.imageFileName.setAcceptDrops(False)
        self.imageFileName.setText("")
        self.imageFileName.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.imageFileName.setReadOnly(True)
        self.imageFileName.setObjectName("imageFileName")
        self.exposeN = QtWidgets.QPushButton(ImageDialog)
        self.exposeN.setGeometry(QtCore.QRect(90, 15, 76, 26))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.exposeN.setFont(font)
        self.exposeN.setObjectName("exposeN")
        self.zoom = QtWidgets.QComboBox(ImageDialog)
        self.zoom.setGeometry(QtCore.QRect(665, 15, 126, 22))
        self.zoom.setCurrentText("")
        self.zoom.setObjectName("zoom")
        self.stretch = QtWidgets.QComboBox(ImageDialog)
        self.stretch.setGeometry(QtCore.QRect(665, 75, 126, 22))
        self.stretch.setCurrentText("")
        self.stretch.setObjectName("stretch")
        self.color = QtWidgets.QComboBox(ImageDialog)
        self.color.setGeometry(QtCore.QRect(665, 45, 126, 22))
        self.color.setCurrentText("")
        self.color.setObjectName("color")
        self.line_71 = QtWidgets.QFrame(ImageDialog)
        self.line_71.setGeometry(QtCore.QRect(5, 120, 791, 1))
        self.line_71.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_71.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_71.setObjectName("line_71")
        self.ra = QtWidgets.QLineEdit(ImageDialog)
        self.ra.setEnabled(False)
        self.ra.setGeometry(QtCore.QRect(465, 15, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.ra.setFont(font)
        self.ra.setMouseTracking(False)
        self.ra.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ra.setAcceptDrops(False)
        self.ra.setText("")
        self.ra.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ra.setReadOnly(True)
        self.ra.setObjectName("ra")
        self.dec = QtWidgets.QLineEdit(ImageDialog)
        self.dec.setEnabled(False)
        self.dec.setGeometry(QtCore.QRect(465, 40, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.dec.setFont(font)
        self.dec.setMouseTracking(False)
        self.dec.setFocusPolicy(QtCore.Qt.NoFocus)
        self.dec.setAcceptDrops(False)
        self.dec.setText("")
        self.dec.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dec.setReadOnly(True)
        self.dec.setObjectName("dec")
        self.scale = QtWidgets.QLineEdit(ImageDialog)
        self.scale.setEnabled(False)
        self.scale.setGeometry(QtCore.QRect(465, 65, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.scale.setFont(font)
        self.scale.setMouseTracking(False)
        self.scale.setFocusPolicy(QtCore.Qt.NoFocus)
        self.scale.setAcceptDrops(False)
        self.scale.setText("")
        self.scale.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.scale.setReadOnly(True)
        self.scale.setObjectName("scale")
        self.ccdTemp = QtWidgets.QLineEdit(ImageDialog)
        self.ccdTemp.setEnabled(False)
        self.ccdTemp.setGeometry(QtCore.QRect(465, 90, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.ccdTemp.setFont(font)
        self.ccdTemp.setMouseTracking(False)
        self.ccdTemp.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ccdTemp.setAcceptDrops(False)
        self.ccdTemp.setText("")
        self.ccdTemp.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ccdTemp.setReadOnly(True)
        self.ccdTemp.setObjectName("ccdTemp")
        self.checkShowCrosshairs = QtWidgets.QCheckBox(ImageDialog)
        self.checkShowCrosshairs.setGeometry(QtCore.QRect(530, 15, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkShowCrosshairs.setFont(font)
        self.checkShowCrosshairs.setChecked(False)
        self.checkShowCrosshairs.setObjectName("checkShowCrosshairs")
        self.checkShowCrosshairs_2 = QtWidgets.QCheckBox(ImageDialog)
        self.checkShowCrosshairs_2.setGeometry(QtCore.QRect(530, 40, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkShowCrosshairs_2.setFont(font)
        self.checkShowCrosshairs_2.setChecked(False)
        self.checkShowCrosshairs_2.setObjectName("checkShowCrosshairs_2")
        self.label_29 = QtWidgets.QLabel(ImageDialog)
        self.label_29.setGeometry(QtCore.QRect(420, 15, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(ImageDialog)
        self.label_30.setGeometry(QtCore.QRect(420, 40, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(ImageDialog)
        self.label_31.setGeometry(QtCore.QRect(420, 65, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(ImageDialog)
        self.label_32.setGeometry(QtCore.QRect(420, 90, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")

        self.retranslateUi(ImageDialog)
        QtCore.QMetaObject.connectSlotsByName(ImageDialog)

    def retranslateUi(self, ImageDialog):
        _translate = QtCore.QCoreApplication.translate
        ImageDialog.setWindowTitle(_translate("ImageDialog", "Imaging"))
        self.expose.setToolTip(_translate("ImageDialog", "<html><head/><body><p>Single exposure</p></body></html>"))
        self.expose.setText(_translate("ImageDialog", "Expose 1"))
        self.solve.setToolTip(_translate("ImageDialog", "<html><head/><body><p>Single plate solve of the actual image</p></body></html>"))
        self.solve.setText(_translate("ImageDialog", "Solve"))
        self.load.setToolTip(_translate("ImageDialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Load a fits file and display is</span></p></body></html>"))
        self.load.setText(_translate("ImageDialog", "Load FITS"))
        self.cancel.setToolTip(_translate("ImageDialog", "<html><head/><body><p>Cancels an imaging or plate solving action or stops continous exposures</p></body></html>"))
        self.cancel.setText(_translate("ImageDialog", "Cancel"))
        self.imageFileName.setToolTip(_translate("ImageDialog", "<html><head/><body><p>name of image which is shown</p></body></html>"))
        self.exposeN.setToolTip(_translate("ImageDialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Continous exposures</span></p></body></html>"))
        self.exposeN.setText(_translate("ImageDialog", "Expose N"))
        self.ra.setToolTip(_translate("ImageDialog", "<html><head/><body><p><span style=\" font-weight:400;\">Shows the solved RA of image in J2000 coordinates</span></p></body></html>"))
        self.dec.setToolTip(_translate("ImageDialog", "<html><head/><body><p><span style=\" font-weight:400;\">Shows the solved RA of image in J2000 coordinates</span></p></body></html>"))
        self.scale.setToolTip(_translate("ImageDialog", "<html><head/><body><p><span style=\" font-weight:400;\">Shows the solved RA of image in J2000 coordinates</span></p></body></html>"))
        self.ccdTemp.setToolTip(_translate("ImageDialog", "<html><head/><body><p><span style=\" font-weight:400;\">Shows the solved RA of image in J2000 coordinates</span></p></body></html>"))
        self.checkShowCrosshairs.setToolTip(_translate("ImageDialog", "<html><head/><body><p>Show crosshairs on image</p></body></html>"))
        self.checkShowCrosshairs.setText(_translate("ImageDialog", "Show crosshairs"))
        self.checkShowCrosshairs_2.setToolTip(_translate("ImageDialog", "<html><head/><body><p>Show crosshairs on image</p></body></html>"))
        self.checkShowCrosshairs_2.setText(_translate("ImageDialog", "Show WCS grid"))
        self.label_29.setText(_translate("ImageDialog", "RA"))
        self.label_30.setText(_translate("ImageDialog", "DEC"))
        self.label_31.setText(_translate("ImageDialog", "Scale"))
        self.label_32.setText(_translate("ImageDialog", "Temp"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ImageDialog = QtWidgets.QWidget()
    ui = Ui_ImageDialog()
    ui.setupUi(ImageDialog)
    ImageDialog.show()
    sys.exit(app.exec_())
