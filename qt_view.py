# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt_view.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setAcceptDrops(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.delButton = QtWidgets.QPushButton(self.centralwidget)
        self.delButton.setGeometry(QtCore.QRect(110, 10, 91, 71))
        self.delButton.setMinimumSize(QtCore.QSize(91, 0))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UI/cancel.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delButton.setIcon(icon)
        self.delButton.setIconSize(QtCore.QSize(32, 32))
        self.delButton.setObjectName("delButton")
        self.openButton = QtWidgets.QPushButton(self.centralwidget)
        self.openButton.setGeometry(QtCore.QRect(10, 10, 91, 71))
        self.openButton.setMinimumSize(QtCore.QSize(81, 0))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("UI/add.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.openButton.setIcon(icon1)
        self.openButton.setIconSize(QtCore.QSize(32, 32))
        self.openButton.setObjectName("openButton")
        self.downloadImgCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.downloadImgCheckBox.setGeometry(QtCore.QRect(310, 20, 73, 16))
        self.downloadImgCheckBox.setObjectName("downloadImgCheckBox")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 90, 771, 451))
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(670, 60, 111, 21))
        self.label.setObjectName("label")
        self.runButton = QtWidgets.QPushButton(self.centralwidget)
        self.runButton.setGeometry(QtCore.QRect(210, 10, 91, 71))
        self.runButton.setMinimumSize(QtCore.QSize(91, 0))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("UI/play.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.runButton.setIcon(icon2)
        self.runButton.setIconSize(QtCore.QSize(32, 32))
        self.runButton.setObjectName("runButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action1 = QtWidgets.QAction(MainWindow)
        self.action1.setObjectName("action1")
        self.action3 = QtWidgets.QAction(MainWindow)
        self.action3.setObjectName("action3")
        self.action2 = QtWidgets.QAction(MainWindow)
        self.action2.setObjectName("action2")
        self.action4 = QtWidgets.QAction(MainWindow)
        self.action4.setObjectName("action4")
        self.action5 = QtWidgets.QAction(MainWindow)
        self.action5.setObjectName("action5")
        self.menu.addAction(self.action3)
        self.menu.addAction(self.action4)
        self.menu_2.addAction(self.action1)
        self.menu_3.addAction(self.action2)
        self.menu_3.addAction(self.action5)
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Odvrt"))
        self.delButton.setText(_translate("MainWindow", "刪除全部"))
        self.openButton.setText(_translate("MainWindow", "開啟"))
        self.downloadImgCheckBox.setText(_translate("MainWindow", "下載縮圖"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "檔案路徑"))
        self.label.setText(_translate("MainWindow", "共0個檔案"))
        self.runButton.setText(_translate("MainWindow", "執行"))
        self.menu.setTitle(_translate("MainWindow", "關於"))
        self.menu_2.setTitle(_translate("MainWindow", "檔案"))
        self.menu_3.setTitle(_translate("MainWindow", "選項"))
        self.action1.setText(_translate("MainWindow", "開啟"))
        self.action3.setText(_translate("MainWindow", "作者"))
        self.action3.setToolTip(_translate("MainWindow", "作者"))
        self.action2.setText(_translate("MainWindow", "執行"))
        self.action4.setText(_translate("MainWindow", "關於此程式"))
        self.action5.setText(_translate("MainWindow", "刪除全部"))
