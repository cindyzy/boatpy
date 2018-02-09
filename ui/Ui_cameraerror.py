# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Users\Administrator\boat\ui\cameraerror.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_cameraerror(object):
    def setupUi(self, cameraerror):
        cameraerror.setObjectName("cameraerror")
        cameraerror.resize(400, 97)
        cameraerror.setStyleSheet("background-color: rgb(62, 144,218);")
        self.verticalLayout = QtWidgets.QVBoxLayout(cameraerror)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(cameraerror)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.retranslateUi(cameraerror)
        QtCore.QMetaObject.connectSlotsByName(cameraerror)

    def retranslateUi(self, cameraerror):
        _translate = QtCore.QCoreApplication.translate
        cameraerror.setWindowTitle(_translate("cameraerror", "Dialog"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    cameraerror = QtWidgets.QDialog()
    ui = Ui_cameraerror()
    ui.setupUi(cameraerror)
    cameraerror.show()
    sys.exit(app.exec_())

