# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Users\Administrator\boat\ui\ismanager.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ismanager(object):
    def setupUi(self, ismanager):
        ismanager.setObjectName("ismanager")
        ismanager.resize(400, 186)
        ismanager.setStyleSheet("background-color: rgb(62, 144,218);")
        self.gridLayout = QtWidgets.QGridLayout(ismanager)
        self.gridLayout.setObjectName("gridLayout")
        self.user = QtWidgets.QLineEdit(ismanager)
        self.user.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.user.setInputMask("")
        self.user.setObjectName("user")
        self.gridLayout.addWidget(self.user, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(ismanager)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 2, 1, 1)
        self.label = QtWidgets.QLabel(ismanager)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.password = QtWidgets.QLineEdit(ismanager)
        self.password.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.gridLayout.addWidget(self.password, 1, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(ismanager)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 4)
        self.pushButton = QtWidgets.QPushButton(ismanager)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 20))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("border-image: url(:/res/button3.png)")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 3, 1, 1)

        self.retranslateUi(ismanager)
        QtCore.QMetaObject.connectSlotsByName(ismanager)

    def retranslateUi(self, ismanager):
        _translate = QtCore.QCoreApplication.translate
        ismanager.setWindowTitle(_translate("ismanager", "Dialog"))
        self.label_2.setText(_translate("ismanager", "密码："))
        self.label.setText(_translate("ismanager", "用户名："))
        self.label_3.setText(_translate("ismanager", "请输入管理员用户名和密码"))
        self.pushButton.setText(_translate("ismanager", "登陆"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ismanager = QtWidgets.QDialog()
    ui = Ui_ismanager()
    ui.setupUi(ismanager)
    ismanager.show()
    sys.exit(app.exec_())

