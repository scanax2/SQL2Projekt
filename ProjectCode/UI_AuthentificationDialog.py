# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_AuthentificationDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog

import repository
from UI_ErrorDialog import UI_ErrorDialog


class UI_AuthentificationDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setObjectName("Dialog")
        self.resize(320, 240)
        self.authBox = QtWidgets.QDialogButtonBox(self)
        self.authBox.setGeometry(QtCore.QRect(90, 170, 151, 32))
        self.authBox.setOrientation(QtCore.Qt.Horizontal)
        self.authBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.authBox.setObjectName("authBox")
        self.loginInput = QtWidgets.QLineEdit(self)
        self.loginInput.setGeometry(QtCore.QRect(90, 60, 151, 20))
        self.loginInput.setObjectName("loginInput")
        self.passwordInput = QtWidgets.QLineEdit(self)
        self.passwordInput.setGeometry(QtCore.QRect(90, 120, 151, 20))
        self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordInput.setObjectName("passwordInput")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(90, 40, 71, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(90, 100, 91, 16))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(self)
        self.authBox.accepted.connect(self.tryAccept) # type: ignore
        self.authBox.rejected.connect(self.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(self)

    def tryAccept(self):
        login = self.loginInput.text()
        password = self.passwordInput.text()
        is_ok = repository.connect_with_database(True, login, password)

        if (is_ok):
            self.accept()
        else:
            self.showErrorDialog("AUTH", "Authentification failed")

        print(is_ok)
        print(login)
        print(password)

    def showErrorDialog(self, type, name):
        errorDialog = UI_ErrorDialog(type, name)
        retValue = errorDialog.exec_()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.loginInput.setText(_translate("Dialog", "inf143187"))
        self.passwordInput.setText(_translate("Dialog", "124124124124"))
        self.label.setText(_translate("Dialog", "Enter login:"))
        self.label_2.setText(_translate("Dialog", "Enter password:"))

        self.loginInput.setText('')
        self.passwordInput.setText('')
