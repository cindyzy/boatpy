# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Users\Administrator\boat\ui\kh.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_kh(object):
    def setupUi(self, kh):
        kh.setObjectName("kh")
        kh.resize(331, 218)
        kh.setStyleSheet("background-color: rgb(62, 144,218);")
        self.centralwidget = QtWidgets.QWidget(kh)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.state = QtWidgets.QGroupBox(self.centralwidget)
        self.state.setMinimumSize(QtCore.QSize(300, 200))
        self.state.setObjectName("state")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.state)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout.addWidget(self.state)
        kh.setCentralWidget(self.centralwidget)

        self.retranslateUi(kh)
        QtCore.QMetaObject.connectSlotsByName(kh)

    def retranslateUi(self, kh):
        _translate = QtCore.QCoreApplication.translate
        kh.setWindowTitle(_translate("kh", "MainWindow"))
        self.state.setTitle(_translate("kh", "状态栏"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    kh = QtWidgets.QMainWindow()
    ui = Ui_kh()
    ui.setupUi(kh)
    kh.show()
    sys.exit(app.exec_())

