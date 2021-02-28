from PyQt5.QtWidgets import QWidget
from Ui.Ui_Team import Ui_FormTeam
from FormMember import FormMember

class FormTeam(QWidget,Ui_FormTeam):
    def __init__(self, parent = None, teamNo = '第一队', team = None):
        super().__init__(parent)
        self.teamNo = teamNo
        self.setupUi(self)

    def setupUi(self,parent):
        super().setupUi(self)
        self.labelTeamNo.setText(self.teamNo)