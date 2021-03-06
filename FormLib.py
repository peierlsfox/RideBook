from SanItemModel import SanItemModel
from PyQt5.QtWidgets import QHeaderView, QWidget
from Ui.Ui_Lib import Ui_FormLib
from SanItemModel import SanItemModel


class FormLib(QWidget,Ui_FormLib):
    def __init__(self, parent = None, libName = '武将库'):
        super().__init__(parent)
        self.libName = libName
        self.setupUi(self)
        

    def setupUi(self,parent):
        super().setupUi(self)
        self.labelLibName.setText(self.libName)
        self.tableViewLib.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
