import DataBase
from Ui.Ui_MainWindow import Ui_MainWindow
import sys
from PyQt5.QtWidgets import QApplication, QHeaderView,QMainWindow
from FormTeam import FormTeam
from PyQt5 import QtCore, QtGui, QtWidgets
from TableModels import SanObjTable
from DataBase import DataBase
from SanHelp import SanHelp

class MyWindow(QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        db = DataBase()
        for i in range(1,11):
            self.widgetTeam = FormTeam(self.scrollAreaWidgetContentsTeams)
            self.widgetTeam.setObjectName('widgetTeam{}'.format(i))
            self.widgetTeam.setTeam(db.getTeamById(i))
            self.verticalLayoutTeams.addWidget(self.widgetTeam, 0, QtCore.Qt.AlignTop)
        self.widgetHeros.labelItemsName.setText('武将库')
        self.widgetMagics.labelItemsName.setText('战法库')
        
        headers, datas = db.exportHerosToTable()
        HeroTableModel = SanObjTable(headers,datas)
        self.widgetHeros.tableViewItems.setModel(HeroTableModel)
        self.widgetHeros.tableViewItems.setType(SanHelp.HeroType)
        self.widgetHeros.tableViewItems.setAddress('LibHero')

        headers, datas = db.exportMagicsToTable()
        MagicTableModel = SanObjTable(headers,datas)
        self.widgetMagics.tableViewItems.setModel(MagicTableModel)
        self.widgetMagics.tableViewItems.setType(SanHelp.MagicType)
        self.widgetMagics.tableViewItems.setAddress('LibMagic')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    sys.exit(app.exec_())