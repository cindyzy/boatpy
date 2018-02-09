# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Users\Administrator\boat\ui\picshow.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_picshow(object):
    def setupUi(self, picshow):
        picshow.setObjectName("picshow")
        picshow.resize(711, 495)
        picshow.setStyleSheet("background-color: rgb(62, 144,218);")
        self.label = QtWidgets.QLabel(picshow)
        self.label.setGeometry(QtCore.QRect(0, 0, 711, 471))
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setObjectName("label")

        self.retranslateUi(picshow)
        QtCore.QMetaObject.connectSlotsByName(picshow)

    def retranslateUi(self, picshow):
        _translate = QtCore.QCoreApplication.translate
        picshow.setWindowTitle(_translate("picshow", "Dialog"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    picshow = QtWidgets.QDialog()
    ui = Ui_picshow()
    ui.setupUi(picshow)
    picshow.show()
    sys.exit(app.exec_())

