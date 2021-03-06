from DataBase import DataBase
from Ui.Ui_SanTool import Ui_MainWindow
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys
from FormTeam import FormTeam
from FormLib import FormLib
from DataBase import DataBase
from SanItemModel import SanItemModel

class SanToolWindow(Ui_MainWindow,QMainWindow):

    chineseNum = ['','一','二','三','四','五','六','七','八','九','十']
    def __init__(self, parent = None):
        super().__init__(parent)
        self.dataBase = DataBase()
        self.setupUi()

    def setupUi(self):
        super().setupUi(self)
        self.resize(1800,1500)
        self.splitter.setSizes([1200,600])
        self.formsTeam = []
        for team in self.dataBase.teams:
            formTeam = FormTeam(self.scrollAreaWidgetTeams,team)
            self.verticalLayoutTeams.addWidget(formTeam)
            self.formsTeam.append(formTeam)

        self.heroLib = FormLib(self.scrollAreaLibs,'武将库')
        headers,datas = self.dataBase.exportHeros()
        heroLibModel = SanItemModel(headers,datas)
        self.heroLib.tableViewLib.setModel(heroLibModel)
        self.heroLib.tableViewLib.setType('hero')
        self.verticalLayoutLibs.addWidget(self.heroLib)
        
        self.magicLib = FormLib(self.scrollAreaLibs,'战法库')
        self.verticalLayoutLibs.addWidget(self.magicLib)     
        headers, datas = self.dataBase.exportMagics()
        magicLibModel =  SanItemModel(headers,datas)
        self.magicLib.tableViewLib.setModel(magicLibModel)
        self.magicLib.tableViewLib.setType('magic')
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = SanToolWindow()
    win.show()
    sys.exit(app.exec_())