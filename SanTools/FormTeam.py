from PyQt5.QtWidgets import QWidget
from Ui_W_Team import Ui_FormTeam
from FormMember import FormMember

class FormTeam(QWidget,Ui_FormTeam):
    def __init__(self, withinView) -> None:
        super().__init__(withinView)
        self.setupUi(self)
        self.member1.setPosition('主')
        self.member2.setPosition('副')
        self.member3.setPosition('副')

    def setTeamNo(self,teamNo):
        self.labelTeamNo.setText(teamNo)