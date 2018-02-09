# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Users\Administrator\boat\ui\remoteip.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_remoteip(object):
    def setupUi(self, remoteip):
        remoteip.setObjectName("remoteip")
        remoteip.resize(400, 62)
        remoteip.setStyleSheet("background-color: rgb(62, 144,218);")
        self.horizontalLayout = QtWidgets.QHBoxLayout(remoteip)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(remoteip)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(remoteip)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.buttonBox = QtWidgets.QDialogButtonBox(remoteip)
        self.buttonBox.setMinimumSize(QtCore.QSize(160, 20))
        self.buttonBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonBox.setStyleSheet("")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)

        self.retranslateUi(remoteip)
        self.buttonBox.accepted.connect(remoteip.accept)
        self.buttonBox.rejected.connect(remoteip.reject)
        QtCore.QMetaObject.connectSlotsByName(remoteip)

    def retranslateUi(self, remoteip):
        _translate = QtCore.QCoreApplication.translate
        remoteip.setWindowTitle(_translate("remoteip", "Dialog"))
        self.label.setText(_translate("remoteip", "服务器："))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    remoteip = QtWidgets.QDialog()
    ui = Ui_remoteip()
    ui.setupUi(remoteip)
    remoteip.show()
    sys.exit(app.exec_())

