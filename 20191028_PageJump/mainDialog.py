# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainDialog(object):
    def setupUi(self, mainDialog):
        mainDialog.setObjectName("mainDialog")
        mainDialog.setWindowModality(QtCore.Qt.NonModal)
        mainDialog.resize(400, 300)
        self.setParamsButton = QtWidgets.QPushButton(mainDialog)
        self.setParamsButton.setGeometry(QtCore.QRect(310, 190, 56, 17))
        self.setParamsButton.setObjectName("setParamsButton")
        self.closeButton = QtWidgets.QPushButton(mainDialog)
        self.closeButton.setGeometry(QtCore.QRect(310, 220, 56, 17))
        self.closeButton.setObjectName("closeButton")
        self.textBrowser = QtWidgets.QTextBrowser(mainDialog)
        self.textBrowser.setGeometry(QtCore.QRect(30, 20, 261, 221))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(mainDialog)
        self.closeButton.clicked.connect(mainDialog.close)
        QtCore.QMetaObject.connectSlotsByName(mainDialog)

    def retranslateUi(self, mainDialog):
        _translate = QtCore.QCoreApplication.translate
        mainDialog.setWindowTitle(_translate("mainDialog", "Dialog"))
        self.setParamsButton.setText(_translate("mainDialog", "SetParams"))
        self.closeButton.setText(_translate("mainDialog", "Close"))
