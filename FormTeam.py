from PyQt5.QtWidgets import QWidget
from Ui.Ui_Team import Ui_FormTeam
from FormMember import FormMember
from Models import *

class FormTeam(QWidget,Ui_FormTeam):
    def __init__(self, withinView) -> None:
        super().__init__(withinView)
        self.setupUi(self)
        self.member1.setPosition('主')
        self.member2.setPosition('副')
        self.member3.setPosition('副')

    def setTeamNo(self,teamNo):
        self.labelTeamNo.setText('第{}队'.format(teamNo))
        self.member1.setAddress('{}.{}'.format(teamNo,1))
        self.member2.setAddress('{}.{}'.format(teamNo,2))
        self.member3.setAddress('{}.{}'.format(teamNo,3))

    def setTeam(self, team:Team):
        if team:
            self.setTeamNo(team.id)
            # self.comboBoxType.setText(team.type)
            self.member1.setMember(team.member1)
            self.member2.setMember(team.member2)
            self.member3.setMember(team.member3)
