# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_AcceptDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog


class UI_AcceptDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setObjectName("Dialog")
        self.resize(244, 196)
        self.acceptBox = QtWidgets.QDialogButtonBox(self)
        self.acceptBox.setGeometry(QtCore.QRect(50, 100, 161, 41))
        self.acceptBox.setOrientation(QtCore.Qt.Horizontal)
        self.acceptBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.acceptBox.setObjectName("acceptBox")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(80, 50, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(self)
        self.acceptBox.accepted.connect(self.accept) # type: ignore
        self.acceptBox.rejected.connect(self.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(self)

        #self.callFunc = func

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Are you sure ?"))
