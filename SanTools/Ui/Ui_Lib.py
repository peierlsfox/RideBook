# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Documents\My Code\python\SanTools\DesignerFile\Lib.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormLib(object):
    def setupUi(self, FormLib):
        FormLib.setObjectName("FormLib")
        FormLib.resize(276, 260)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FormLib.sizePolicy().hasHeightForWidth())
        FormLib.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(FormLib)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelLibName = QtWidgets.QLabel(FormLib)
        self.labelLibName.setObjectName("labelLibName")
        self.horizontalLayout.addWidget(self.labelLibName)
        self.lineEditFilter = QtWidgets.QLineEdit(FormLib)
        self.lineEditFilter.setText("")
        self.lineEditFilter.setObjectName("lineEditFilter")
        self.horizontalLayout.addWidget(self.lineEditFilter)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableViewLib = QtWidgets.QTableView(FormLib)
        self.tableViewLib.setObjectName("tableViewLib")
        self.verticalLayout.addWidget(self.tableViewLib)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(FormLib)
        QtCore.QMetaObject.connectSlotsByName(FormLib)

    def retranslateUi(self, FormLib):
        _translate = QtCore.QCoreApplication.translate
        FormLib.setWindowTitle(_translate("FormLib", "Form"))
        self.labelLibName.setText(_translate("FormLib", "库名称"))
        self.lineEditFilter.setPlaceholderText(_translate("FormLib", "搜索"))
