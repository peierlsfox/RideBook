# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\My Data\01 My Code\python\SanTools\Designer\Member.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormMember(object):
    def setupUi(self, FormMember):
        FormMember.setObjectName("FormMember")
        FormMember.resize(173, 105)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FormMember.sizePolicy().hasHeightForWidth())
        FormMember.setSizePolicy(sizePolicy)
        FormMember.setAcceptDrops(True)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(FormMember)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(9, 0, 9, 0)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelMemberPosition = QtWidgets.QLabel(FormMember)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelMemberPosition.sizePolicy().hasHeightForWidth())
        self.labelMemberPosition.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("华文隶书")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.labelMemberPosition.setFont(font)
        self.labelMemberPosition.setStyleSheet("color: rgb(156, 156, 156);\n"
"color: rgb(200, 228, 200);")
        self.labelMemberPosition.setTextFormat(QtCore.Qt.AutoText)
        self.labelMemberPosition.setScaledContents(False)
        self.labelMemberPosition.setAlignment(QtCore.Qt.AlignCenter)
        self.labelMemberPosition.setObjectName("labelMemberPosition")
        self.horizontalLayout.addWidget(self.labelMemberPosition)
        self.labelHeroName = DragableLabel(FormMember)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelHeroName.sizePolicy().hasHeightForWidth())
        self.labelHeroName.setSizePolicy(sizePolicy)
        self.labelHeroName.setMinimumSize(QtCore.QSize(70, 25))
        self.labelHeroName.setAcceptDrops(True)
        self.labelHeroName.setFrameShape(QtWidgets.QFrame.Box)
        self.labelHeroName.setAlignment(QtCore.Qt.AlignCenter)
        self.labelHeroName.setObjectName("labelHeroName")
        self.horizontalLayout.addWidget(self.labelHeroName, 0, QtCore.Qt.AlignVCenter)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.labelMagic1 = QtWidgets.QLabel(FormMember)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelMagic1.sizePolicy().hasHeightForWidth())
        self.labelMagic1.setSizePolicy(sizePolicy)
        self.labelMagic1.setMinimumSize(QtCore.QSize(0, 20))
        self.labelMagic1.setFrameShape(QtWidgets.QFrame.Box)
        self.labelMagic1.setAlignment(QtCore.Qt.AlignCenter)
        self.labelMagic1.setObjectName("labelMagic1")
        self.verticalLayout.addWidget(self.labelMagic1, 0, QtCore.Qt.AlignVCenter)
        self.labelMagic2 = DragableLabel(FormMember)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelMagic2.sizePolicy().hasHeightForWidth())
        self.labelMagic2.setSizePolicy(sizePolicy)
        self.labelMagic2.setMinimumSize(QtCore.QSize(0, 20))
        self.labelMagic2.setAcceptDrops(True)
        self.labelMagic2.setFrameShape(QtWidgets.QFrame.Box)
        self.labelMagic2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelMagic2.setObjectName("labelMagic2")
        self.verticalLayout.addWidget(self.labelMagic2, 0, QtCore.Qt.AlignVCenter)
        self.labelMagic3 = DragableLabel(FormMember)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelMagic3.sizePolicy().hasHeightForWidth())
        self.labelMagic3.setSizePolicy(sizePolicy)
        self.labelMagic3.setMinimumSize(QtCore.QSize(0, 20))
        self.labelMagic3.setAcceptDrops(True)
        self.labelMagic3.setFrameShape(QtWidgets.QFrame.Box)
        self.labelMagic3.setAlignment(QtCore.Qt.AlignCenter)
        self.labelMagic3.setObjectName("labelMagic3")
        self.verticalLayout.addWidget(self.labelMagic3, 0, QtCore.Qt.AlignVCenter)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(FormMember)
        QtCore.QMetaObject.connectSlotsByName(FormMember)

    def retranslateUi(self, FormMember):
        _translate = QtCore.QCoreApplication.translate
        FormMember.setWindowTitle(_translate("FormMember", "Form"))
        self.labelMemberPosition.setText(_translate("FormMember", "主"))
        self.labelHeroName.setText(_translate("FormMember", "武将"))
        self.labelMagic1.setText(_translate("FormMember", "战法一"))
        self.labelMagic2.setText(_translate("FormMember", "战法二"))
        self.labelMagic3.setText(_translate("FormMember", "战法三"))
from DragableLabel import DragableLabel
