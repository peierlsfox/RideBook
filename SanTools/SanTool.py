from DataBase import DataBase
from Ui.Ui_SanTool import Ui_MainWindow
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys
from FormTeam import FormTeam
from FormLib import FormLib
from DataBase import DataBase

class SanToolWindow(Ui_MainWindow,QMainWindow):

    chineseNum = ['','一','二','三','四','五','六','七','八','九','十']
    def __init__(self, parent = None):
        super().__init__(parent)
        self.dataBase = DataBase()
        self.setupUi()

    def setupUi(self):
        super().setupUi(self)
        self.resize(1280,1024)
        self.splitter.setSizes([100,200])
        self.formsTeam = []
        for team in self.dataBase.teams:
            teamNo = team.name
            formTeam = FormTeam(self.scrollAreaWidgetTeams,teamNo)
            self.verticalLayoutTeams.addWidget(formTeam)
            self.formsTeam.append(formTeam)
        self.heroLib = FormLib(self.scrollAreaLibs,'武将库')
        self.verticalLayoutLibs.addWidget(self.heroLib)
        self.magicLib = FormLib(self.scrollAreaLibs,'战法库')
        self.verticalLayoutLibs.addWidget(self.magicLib)        
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = SanToolWindow()
    win.show()
    sys.exit(app.exec_())