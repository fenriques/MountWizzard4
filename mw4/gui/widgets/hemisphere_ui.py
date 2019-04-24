# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hemisphere.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HemisphereDialog(object):
    def setupUi(self, HemisphereDialog):
        HemisphereDialog.setObjectName("HemisphereDialog")
        HemisphereDialog.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(HemisphereDialog.sizePolicy().hasHeightForWidth())
        HemisphereDialog.setSizePolicy(sizePolicy)
        HemisphereDialog.setMinimumSize(QtCore.QSize(800, 400))
        HemisphereDialog.setMaximumSize(QtCore.QSize(1600, 1200))
        HemisphereDialog.setSizeIncrement(QtCore.QSize(10, 10))
        HemisphereDialog.setBaseSize(QtCore.QSize(10, 10))
        font = QtGui.QFont()
        font.setFamily("Arial")
        HemisphereDialog.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(HemisphereDialog)
        self.verticalLayout.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(4, 4, 4, 4)
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.clearBuildP = QtWidgets.QPushButton(HemisphereDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearBuildP.sizePolicy().hasHeightForWidth())
        self.clearBuildP.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.clearBuildP.setFont(font)
        self.clearBuildP.setObjectName("clearBuildP")
        self.horizontalLayout.addWidget(self.clearBuildP)
        self.line_2 = QtWidgets.QFrame(HemisphereDialog)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setMidLineWidth(1)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout.addWidget(self.line_2)
        self.groupBox_3 = QtWidgets.QGroupBox(HemisphereDialog)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setContentsMargins(10, 4, 10, 4)
        self.verticalLayout_2.setSpacing(4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkShowAlignStar = QtWidgets.QCheckBox(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkShowAlignStar.setFont(font)
        self.checkShowAlignStar.setObjectName("checkShowAlignStar")
        self.verticalLayout_2.addWidget(self.checkShowAlignStar)
        self.checkShowMeridian = QtWidgets.QCheckBox(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkShowMeridian.setFont(font)
        self.checkShowMeridian.setObjectName("checkShowMeridian")
        self.verticalLayout_2.addWidget(self.checkShowMeridian)
        self.checkShowCelestial = QtWidgets.QCheckBox(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkShowCelestial.setFont(font)
        self.checkShowCelestial.setObjectName("checkShowCelestial")
        self.verticalLayout_2.addWidget(self.checkShowCelestial)
        self.checkShowSlewPath = QtWidgets.QCheckBox(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkShowSlewPath.setFont(font)
        self.checkShowSlewPath.setObjectName("checkShowSlewPath")
        self.verticalLayout_2.addWidget(self.checkShowSlewPath)
        self.checkUseHorizon = QtWidgets.QCheckBox(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkUseHorizon.setFont(font)
        self.checkUseHorizon.setChecked(False)
        self.checkUseHorizon.setObjectName("checkUseHorizon")
        self.verticalLayout_2.addWidget(self.checkUseHorizon)
        self.horizontalLayout.addWidget(self.groupBox_3)
        self.line_3 = QtWidgets.QFrame(HemisphereDialog)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setMidLineWidth(1)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout.addWidget(self.line_3)
        self.groupBox_2 = QtWidgets.QGroupBox(HemisphereDialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setContentsMargins(10, 4, 10, 4)
        self.verticalLayout_3.setSpacing(4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.checkEditNone = QtWidgets.QRadioButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkEditNone.setFont(font)
        self.checkEditNone.setChecked(True)
        self.checkEditNone.setObjectName("checkEditNone")
        self.verticalLayout_3.addWidget(self.checkEditNone)
        self.checkEditBuildPoints = QtWidgets.QRadioButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkEditBuildPoints.setFont(font)
        self.checkEditBuildPoints.setObjectName("checkEditBuildPoints")
        self.verticalLayout_3.addWidget(self.checkEditBuildPoints)
        self.checkEditHorizonMask = QtWidgets.QRadioButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkEditHorizonMask.setFont(font)
        self.checkEditHorizonMask.setObjectName("checkEditHorizonMask")
        self.verticalLayout_3.addWidget(self.checkEditHorizonMask)
        self.checkPolarAlignment = QtWidgets.QRadioButton(self.groupBox_2)
        self.checkPolarAlignment.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkPolarAlignment.setFont(font)
        self.checkPolarAlignment.setObjectName("checkPolarAlignment")
        self.verticalLayout_3.addWidget(self.checkPolarAlignment)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.line_4 = QtWidgets.QFrame(HemisphereDialog)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_4.setMidLineWidth(1)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout.addWidget(self.line_4)
        self.groupBox = QtWidgets.QGroupBox(HemisphereDialog)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setContentsMargins(4, 4, 4, 4)
        self.horizontalLayout_2.setSpacing(4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setSpacing(4)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.points = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.points.sizePolicy().hasHeightForWidth())
        self.points.setSizePolicy(sizePolicy)
        self.points.setMinimumSize(QtCore.QSize(0, 20))
        self.points.setMaximumSize(QtCore.QSize(40, 20))
        self.points.setObjectName("points")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.points)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.solved = QtWidgets.QLabel(self.groupBox)
        self.solved.setObjectName("solved")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.solved)
        self.slewed = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slewed.sizePolicy().hasHeightForWidth())
        self.slewed.setSizePolicy(sizePolicy)
        self.slewed.setMinimumSize(QtCore.QSize(0, 20))
        self.slewed.setMaximumSize(QtCore.QSize(40, 20))
        self.slewed.setObjectName("slewed")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.slewed)
        self.imaged = QtWidgets.QLineEdit(self.groupBox)
        self.imaged.setMinimumSize(QtCore.QSize(0, 20))
        self.imaged.setMaximumSize(QtCore.QSize(40, 20))
        self.imaged.setObjectName("imaged")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.imaged)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy)
        self.lineEdit_4.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEdit_4.setMaximumSize(QtCore.QSize(40, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        self.horizontalLayout_2.addLayout(self.formLayout)
        spacerItem = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setObjectName("widget")
        self.verticalLayout_5.addWidget(self.widget)
        self.slewedBar = QtWidgets.QProgressBar(self.groupBox)
        self.slewedBar.setMinimumSize(QtCore.QSize(0, 20))
        self.slewedBar.setMaximumSize(QtCore.QSize(16777215, 20))
        self.slewedBar.setProperty("value", 24)
        self.slewedBar.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.slewedBar.setTextVisible(False)
        self.slewedBar.setObjectName("slewedBar")
        self.verticalLayout_5.addWidget(self.slewedBar)
        self.imagedBar = QtWidgets.QProgressBar(self.groupBox)
        self.imagedBar.setMinimumSize(QtCore.QSize(0, 20))
        self.imagedBar.setMaximumSize(QtCore.QSize(16777215, 20))
        self.imagedBar.setProperty("value", 24)
        self.imagedBar.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.imagedBar.setTextVisible(False)
        self.imagedBar.setObjectName("imagedBar")
        self.verticalLayout_5.addWidget(self.imagedBar)
        self.solvedBar = QtWidgets.QProgressBar(self.groupBox)
        self.solvedBar.setMaximumSize(QtCore.QSize(16777215, 20))
        self.solvedBar.setProperty("value", 24)
        self.solvedBar.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.solvedBar.setTextVisible(False)
        self.solvedBar.setObjectName("solvedBar")
        self.verticalLayout_5.addWidget(self.solvedBar)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.horizontalLayout_2.setStretch(2, 1)
        self.horizontalLayout.addWidget(self.groupBox)
        self.horizontalLayout.setStretch(6, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line = QtWidgets.QFrame(HemisphereDialog)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setMidLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.hemisphere = QtWidgets.QWidget(HemisphereDialog)
        self.hemisphere.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hemisphere.sizePolicy().hasHeightForWidth())
        self.hemisphere.setSizePolicy(sizePolicy)
        self.hemisphere.setMinimumSize(QtCore.QSize(790, 270))
        self.hemisphere.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.hemisphere.setSizeIncrement(QtCore.QSize(10, 10))
        self.hemisphere.setBaseSize(QtCore.QSize(10, 10))
        self.hemisphere.setAutoFillBackground(True)
        self.hemisphere.setStyleSheet("")
        self.hemisphere.setObjectName("hemisphere")
        self.verticalLayout.addWidget(self.hemisphere)
        self.verticalLayout.setStretch(2, 1)

        self.retranslateUi(HemisphereDialog)
        QtCore.QMetaObject.connectSlotsByName(HemisphereDialog)

    def retranslateUi(self, HemisphereDialog):
        _translate = QtCore.QCoreApplication.translate
        HemisphereDialog.setWindowTitle(_translate("HemisphereDialog", "Hemisphere"))
        self.clearBuildP.setToolTip(_translate("HemisphereDialog", "<html><head/><body><p>Delete all points on coordinate window including Base / Model</p></body></html>"))
        self.clearBuildP.setText(_translate("HemisphereDialog", "Clear Points"))
        self.groupBox_3.setTitle(_translate("HemisphereDialog", "Setup"))
        self.checkShowAlignStar.setText(_translate("HemisphereDialog", "Show align stars"))
        self.checkShowMeridian.setText(_translate("HemisphereDialog", "Show meridian limits"))
        self.checkShowCelestial.setText(_translate("HemisphereDialog", "Show celestial paths"))
        self.checkShowSlewPath.setText(_translate("HemisphereDialog", "Show slew path"))
        self.checkUseHorizon.setToolTip(_translate("HemisphereDialog", "<html><head/><body><p>Use horizon mask file in hemisphere window.</p></body></html>"))
        self.checkUseHorizon.setText(_translate("HemisphereDialog", "Show horizon mask"))
        self.groupBox_2.setTitle(_translate("HemisphereDialog", "Operation Mode"))
        self.checkEditNone.setText(_translate("HemisphereDialog", "Normal mode"))
        self.checkEditBuildPoints.setText(_translate("HemisphereDialog", "Edit Build Points"))
        self.checkEditHorizonMask.setText(_translate("HemisphereDialog", "Edit Horizon Mask"))
        self.checkPolarAlignment.setText(_translate("HemisphereDialog", "Polar/Ortho Align"))
        self.groupBox.setTitle(_translate("HemisphereDialog", "Mode Build Progress"))
        self.label.setText(_translate("HemisphereDialog", "Points"))
        self.label_2.setText(_translate("HemisphereDialog", "Slewed"))
        self.label_3.setText(_translate("HemisphereDialog", "Imaged"))
        self.solved.setText(_translate("HemisphereDialog", "Solved"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HemisphereDialog = QtWidgets.QWidget()
    ui = Ui_HemisphereDialog()
    ui.setupUi(HemisphereDialog)
    HemisphereDialog.show()
    sys.exit(app.exec_())
