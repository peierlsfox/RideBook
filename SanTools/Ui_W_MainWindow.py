# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\My Data\01 My Code\python\SanTools\W_MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(708, 515)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.scrollAreaItems = QtWidgets.QScrollArea(self.splitter)
        self.scrollAreaItems.setWidgetResizable(True)
        self.scrollAreaItems.setObjectName("scrollAreaItems")
        self.scrollAreaWidgetContentsItems = QtWidgets.QWidget()
        self.scrollAreaWidgetContentsItems.setGeometry(QtCore.QRect(0, 0, 379, 450))
        self.scrollAreaWidgetContentsItems.setObjectName("scrollAreaWidgetContentsItems")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContentsItems)
        self.verticalLayout_3.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widgetHeros = FormItemTable(self.scrollAreaWidgetContentsItems)
        self.widgetHeros.setAcceptDrops(True)
        self.widgetHeros.setObjectName("widgetHeros")
        self.verticalLayout.addWidget(self.widgetHeros)
        self.widgetMagics = FormItemTable(self.scrollAreaWidgetContentsItems)
        self.widgetMagics.setAcceptDrops(True)
        self.widgetMagics.setObjectName("widgetMagics")
        self.verticalLayout.addWidget(self.widgetMagics)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.scrollAreaItems.setWidget(self.scrollAreaWidgetContentsItems)
        self.scrollAreaTeams = QtWidgets.QScrollArea(self.splitter)
        self.scrollAreaTeams.setAcceptDrops(True)
        self.scrollAreaTeams.setWidgetResizable(True)
        self.scrollAreaTeams.setObjectName("scrollAreaTeams")
        self.scrollAreaWidgetContentsTeams = QtWidgets.QWidget()
        self.scrollAreaWidgetContentsTeams.setGeometry(QtCore.QRect(0, 0, 302, 450))
        self.scrollAreaWidgetContentsTeams.setObjectName("scrollAreaWidgetContentsTeams")
        self.verticalLayoutTeams = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContentsTeams)
        self.verticalLayoutTeams.setContentsMargins(3, 3, 3, 3)
        self.verticalLayoutTeams.setSpacing(3)
        self.verticalLayoutTeams.setObjectName("verticalLayoutTeams")
        self.scrollAreaTeams.setWidget(self.scrollAreaWidgetContentsTeams)
        self.verticalLayout_2.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 708, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_2)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "文件(F)"))
        self.actionNew.setText(_translate("MainWindow", "新建"))
        self.action_2.setText(_translate("MainWindow", "退出"))
from FormItemTable import FormItemTable