from PyQt5.QtWidgets import QWidget
from Ui.Ui_Team import Ui_FormTeam
from FormMember import FormMember
from Models.Hero import Hero
from Models.Magic import Magic
from Models.Team import Team
from Models.Member import Member

class FormTeam(QWidget,Ui_FormTeam):
    def __init__(self, parent = None, team:Team = None):
        super().__init__(parent)
        super().setupUi(self)
        self.setTeam(team)
    
    def updateUi(self):
        self.labelTeamNo.setText(self.team.name)
        self.lineEditTeamDesc.setText(self.team.description)
        self.comboBoxType.setCurrentText(self.team.type)
       
    def setTeam(self, team):
        self.team = team
        self.widgetMember1.setMember(self.team.members[0])
        self.widgetMember1.setAddress('{}.{}'.format(self.team.name,1))
        self.widgetMember2.setMember(self.team.members[1])
        self.widgetMember2.setAddress('{}.{}'.format(self.team.name,2))
        self.widgetMember3.setMember(self.team.members[2])
        self.widgetMember3.setAddress('{}.{}'.format(self.team.name,3))
        self.updateUi()