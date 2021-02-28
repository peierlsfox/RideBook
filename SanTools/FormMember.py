from PyQt5.QtWidgets import QWidget
from Ui.Ui_Member import Ui_FormMember

class FormMember(QWidget,Ui_FormMember):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)

    def setupUi(self,parent):
        super().setupUi(self)