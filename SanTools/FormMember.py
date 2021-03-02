from PyQt5.QtWidgets import QWidget
from Ui_W_Member import Ui_FormMember

class FormMember(QWidget,Ui_FormMember):
    def __init__(self, withinView) -> None:
        super(FormMember,self).__init__(withinView)
        self.setupUi(self)

    def setPosition(self,position):
        self.labelMemberPosition.setText(position)

    