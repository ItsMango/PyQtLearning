# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settingDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_settingDialog(object):
    def setupUi(self, settingDialog):
        settingDialog.setObjectName("settingDialog")
        settingDialog.resize(400, 300)
        self.keyLabel = QtWidgets.QLabel(settingDialog)
        self.keyLabel.setGeometry(QtCore.QRect(50, 60, 35, 10))
        self.keyLabel.setObjectName("keyLabel")
        self.valueLabel = QtWidgets.QLabel(settingDialog)
        self.valueLabel.setGeometry(QtCore.QRect(50, 90, 35, 10))
        self.valueLabel.setObjectName("valueLabel")
        self.keyLineEdit = QtWidgets.QLineEdit(settingDialog)
        self.keyLineEdit.setGeometry(QtCore.QRect(100, 50, 113, 20))
        self.keyLineEdit.setObjectName("keyLineEdit")
        self.valueLineEdit = QtWidgets.QLineEdit(settingDialog)
        self.valueLineEdit.setGeometry(QtCore.QRect(100, 90, 113, 20))
        self.valueLineEdit.setObjectName("valueLineEdit")
        self.settinghButton = QtWidgets.QPushButton(settingDialog)
        self.settinghButton.setGeometry(QtCore.QRect(290, 150, 56, 17))
        self.settinghButton.setObjectName("settinghButton")
        self.cancelpushButton = QtWidgets.QPushButton(settingDialog)
        self.cancelpushButton.setGeometry(QtCore.QRect(290, 190, 56, 17))
        self.cancelpushButton.setObjectName("cancelpushButton")

        self.retranslateUi(settingDialog)
        QtCore.QMetaObject.connectSlotsByName(settingDialog)

    def retranslateUi(self, settingDialog):
        _translate = QtCore.QCoreApplication.translate
        settingDialog.setWindowTitle(_translate("settingDialog", "Dialog"))
        self.keyLabel.setText(_translate("settingDialog", "Key       :"))
        self.valueLabel.setText(_translate("settingDialog", "Value    :"))
        self.settinghButton.setText(_translate("settingDialog", "SetParams"))
        self.cancelpushButton.setText(_translate("settingDialog", "Cancel"))
