from DataBase import DataBase
from PyQt5.QtWidgets import QWidget, QHeaderView
from Ui_W_ItemTable import Ui_FormItemTable
from TableModels import SanObjTable

class FormItemTable(QWidget,Ui_FormItemTable):
    def __init__(self, withinView) -> None:
        super(FormItemTable,self).__init__(withinView)
        self.setupUi(self)

    def setupUi(self,parent):
        super().setupUi(self)
        self.tableViewItems.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        # self.tableViewItems.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tableViewItems.setDragEnabled(True)
