# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Users\Administrator\boat\ui\jiance.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEnginePage, QWebEngineView
class Ui_jiance(object):
    def setupUi(self, jiance):
        jiance.setObjectName("jiance")
        jiance.resize(1013, 614)
        jiance.setMinimumSize(QtCore.QSize(995, 0))
        jiance.setMaximumSize(QtCore.QSize(1013, 16777215))
        jiance.setStyleSheet("background-color: rgb(222, 233, 251);")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(jiance)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tabWidget = QtWidgets.QTabWidget(jiance)
        self.tabWidget.setMaximumSize(QtCore.QSize(995, 16777215))
        self.tabWidget.setObjectName("tabWidget")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.widget = QtWidgets.QWidget(self.tab1)
        self.widget.setMinimumSize(QtCore.QSize(0, 0))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.webView_4 =QWebEngineView(self.widget)
        self.webView_4.setMinimumSize(QtCore.QSize(500, 290))
        self.webView_4.setMaximumSize(QtCore.QSize(500, 290))
        self.webView_4.setUrl(QtCore.QUrl("about:blank"))
        self.webView_4.setObjectName("webView_4")
        self.horizontalLayout.addWidget(self.webView_4)
        self.widget_12 = QtWidgets.QWidget(self.widget)
        self.widget_12.setObjectName("widget_12")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget_12)
        self.verticalLayout_8.setContentsMargins(10, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.picture = QtWidgets.QPushButton(self.widget_12)
        self.picture.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.picture.setFlat(True)
        self.picture.setObjectName("picture")
        self.verticalLayout_8.addWidget(self.picture)
        self.horizontalLayout.addWidget(self.widget_12)
        self.gridLayout_3.addWidget(self.widget, 3, 0, 1, 2)
        self.widget_9 = QtWidgets.QWidget(self.tab1)
        self.widget_9.setObjectName("widget_9")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_9)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.temlabel = QtWidgets.QLabel(self.widget_9)
        self.temlabel.setEnabled(True)
        self.temlabel.setMinimumSize(QtCore.QSize(0, 20))
        self.temlabel.setMaximumSize(QtCore.QSize(300, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.temlabel.setFont(font)
        self.temlabel.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.temlabel.setIndent(10)
        self.temlabel.setObjectName("temlabel")
        self.gridLayout.addWidget(self.temlabel, 1, 1, 1, 1)
        self.vislabel = QtWidgets.QLabel(self.widget_9)
        self.vislabel.setEnabled(True)
        self.vislabel.setMinimumSize(QtCore.QSize(0, 20))
        self.vislabel.setMaximumSize(QtCore.QSize(300, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.vislabel.setFont(font)
        self.vislabel.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.vislabel.setIndent(10)
        self.vislabel.setObjectName("vislabel")
        self.gridLayout.addWidget(self.vislabel, 1, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.widget_9)
        self.label_11.setEnabled(True)
        self.label_11.setMinimumSize(QtCore.QSize(0, 20))
        self.label_11.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setIndent(10)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 0, 0, 1, 1)
        self.visreflabel = QtWidgets.QLabel(self.widget_9)
        self.visreflabel.setMinimumSize(QtCore.QSize(0, 20))
        self.visreflabel.setMaximumSize(QtCore.QSize(300, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.visreflabel.setFont(font)
        self.visreflabel.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.visreflabel.setIndent(10)
        self.visreflabel.setObjectName("visreflabel")
        self.gridLayout.addWidget(self.visreflabel, 4, 0, 1, 1)
        self.waterlabel = QtWidgets.QLabel(self.widget_9)
        self.waterlabel.setEnabled(True)
        self.waterlabel.setMinimumSize(QtCore.QSize(0, 20))
        self.waterlabel.setMaximumSize(QtCore.QSize(300, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.waterlabel.setFont(font)
        self.waterlabel.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.waterlabel.setIndent(10)
        self.waterlabel.setObjectName("waterlabel")
        self.gridLayout.addWidget(self.waterlabel, 4, 1, 1, 1)
        self.vischangeratelabel = QtWidgets.QLabel(self.widget_9)
        self.vischangeratelabel.setMinimumSize(QtCore.QSize(0, 20))
        self.vischangeratelabel.setMaximumSize(QtCore.QSize(300, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.vischangeratelabel.setFont(font)
        self.vischangeratelabel.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.vischangeratelabel.setIndent(10)
        self.vischangeratelabel.setObjectName("vischangeratelabel")
        self.gridLayout.addWidget(self.vischangeratelabel, 5, 0, 1, 1)
        self.num_14_21_label = QtWidgets.QLabel(self.widget_9)
        self.num_14_21_label.setEnabled(True)
        self.num_14_21_label.setMinimumSize(QtCore.QSize(0, 20))
        self.num_14_21_label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.num_14_21_label.setFont(font)
        self.num_14_21_label.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.num_14_21_label.setIndent(10)
        self.num_14_21_label.setObjectName("num_14_21_label")
        self.gridLayout.addWidget(self.num_14_21_label, 4, 2, 1, 1)
        self.num_38_70_label = QtWidgets.QLabel(self.widget_9)
        self.num_38_70_label.setEnabled(True)
        self.num_38_70_label.setMinimumSize(QtCore.QSize(0, 20))
        self.num_38_70_label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.num_38_70_label.setFont(font)
        self.num_38_70_label.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.num_38_70_label.setIndent(10)
        self.num_38_70_label.setObjectName("num_38_70_label")
        self.gridLayout.addWidget(self.num_38_70_label, 5, 2, 1, 1)
        self.num_4_6_label = QtWidgets.QLabel(self.widget_9)
        self.num_4_6_label.setEnabled(True)
        self.num_4_6_label.setMinimumSize(QtCore.QSize(0, 20))
        self.num_4_6_label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.num_4_6_label.setFont(font)
        self.num_4_6_label.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.num_4_6_label.setIndent(10)
        self.num_4_6_label.setObjectName("num_4_6_label")
        self.gridLayout.addWidget(self.num_4_6_label, 1, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.widget_9)
        self.label_12.setMinimumSize(QtCore.QSize(0, 20))
        self.label_12.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setIndent(10)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 0, 2, 1, 1)
        self.num_21_38_label = QtWidgets.QLabel(self.widget_9)
        self.num_21_38_label.setEnabled(True)
        self.num_21_38_label.setMinimumSize(QtCore.QSize(0, 20))
        self.num_21_38_label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.num_21_38_label.setFont(font)
        self.num_21_38_label.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.num_21_38_label.setIndent(10)
        self.num_21_38_label.setObjectName("num_21_38_label")
        self.gridLayout.addWidget(self.num_21_38_label, 4, 3, 1, 1)
        self.num_6_14_label = QtWidgets.QLabel(self.widget_9)
        self.num_6_14_label.setEnabled(True)
        self.num_6_14_label.setMinimumSize(QtCore.QSize(0, 20))
        self.num_6_14_label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.num_6_14_label.setFont(font)
        self.num_6_14_label.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.num_6_14_label.setIndent(10)
        self.num_6_14_label.setObjectName("num_6_14_label")
        self.gridLayout.addWidget(self.num_6_14_label, 1, 3, 1, 1)
        self.num_70_up_label = QtWidgets.QLabel(self.widget_9)
        self.num_70_up_label.setEnabled(True)
        self.num_70_up_label.setMinimumSize(QtCore.QSize(0, 20))
        self.num_70_up_label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.num_70_up_label.setFont(font)
        self.num_70_up_label.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.num_70_up_label.setIndent(10)
        self.num_70_up_label.setObjectName("num_70_up_label")
        self.gridLayout.addWidget(self.num_70_up_label, 5, 3, 1, 1)
        self.Num_gradelabel = QtWidgets.QLabel(self.widget_9)
        self.Num_gradelabel.setMinimumSize(QtCore.QSize(0, 20))
        self.Num_gradelabel.setMaximumSize(QtCore.QSize(300, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.Num_gradelabel.setFont(font)
        self.Num_gradelabel.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.Num_gradelabel.setIndent(10)
        self.Num_gradelabel.setObjectName("Num_gradelabel")
        self.gridLayout.addWidget(self.Num_gradelabel, 6, 2, 1, 1)
        self.gridLayout_3.addWidget(self.widget_9, 4, 0, 1, 2)
        self.tabWidget.addTab(self.tab1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.webView = QWebEngineView(self.tab_2)
        self.webView.setObjectName("webView")
        self.gridLayout_6.addWidget(self.webView, 3, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.webView_2 = QWebEngineView(self.tab)
        self.webView_2.setUrl(QtCore.QUrl("about:blank"))
        self.webView_2.setObjectName("webView_2")
        self.verticalLayout.addWidget(self.webView_2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.webView_3 = QWebEngineView(self.tab_3)
        self.webView_3.setUrl(QtCore.QUrl("about:blank"))
        self.webView_3.setObjectName("webView_3")
        self.verticalLayout_3.addWidget(self.webView_3)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_15 = QtWidgets.QLabel(self.tab_4)
        self.label_15.setMinimumSize(QtCore.QSize(0, 20))
        self.label_15.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_4.addWidget(self.label_15)
        self.tableView = QtWidgets.QTableView(self.tab_4)
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableView.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setDefaultSectionSize(80)
        self.tableView.verticalHeader().setVisible(False)
        self.verticalLayout_4.addWidget(self.tableView)
        self.tabWidget.addTab(self.tab_4, "")
        self.verticalLayout_5.addWidget(self.tabWidget)

        self.retranslateUi(jiance)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(jiance)

    def retranslateUi(self, jiance):
        _translate = QtCore.QCoreApplication.translate
        jiance.setWindowTitle(_translate("jiance", "Dialog"))
        self.picture.setText(_translate("jiance", "无图片显示"))
        self.temlabel.setText(_translate("jiance", "温度     (℃)："))
        self.vislabel.setText(_translate("jiance", "实测黏度  (cSt)："))
        self.label_11.setText(_translate("jiance", "监测指标"))
        self.visreflabel.setText(_translate("jiance", "新油黏度  (cSt)："))
        self.waterlabel.setText(_translate("jiance", "水分  (ppm)："))
        self.vischangeratelabel.setText(_translate("jiance", "黏度变化率(%)："))
        self.num_14_21_label.setText(_translate("jiance", "[14,21) um："))
        self.num_38_70_label.setText(_translate("jiance", "[38,70) um："))
        self.num_4_6_label.setText(_translate("jiance", "[  4,  6) um："))
        self.label_12.setText(_translate("jiance", "铁磁性磨粒分布"))
        self.num_21_38_label.setText(_translate("jiance", "[21,38) um："))
        self.num_6_14_label.setText(_translate("jiance", "[  6,14) um："))
        self.num_70_up_label.setText(_translate("jiance", "[70,∞ ) um："))
        self.Num_gradelabel.setText(_translate("jiance", "磨损烈度等级 ："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("jiance", "数据监控"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("jiance", "图表监控"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("jiance", "油液数据分析图"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("jiance", "磨损烈度等级分析图"))
        self.label_15.setText(_translate("jiance", "监测指标表"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("jiance", "监测指标表"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    jiance = QtWidgets.QDialog()
    ui = Ui_jiance()
    ui.setupUi(jiance)
    jiance.show()
    sys.exit(app.exec_())

