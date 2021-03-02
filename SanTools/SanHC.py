import DataBase
from Ui_W_MainWindow import Ui_MainWindow
import sys
from PyQt5.QtWidgets import QApplication, QHeaderView,QMainWindow
from FormTeam import FormTeam
from PyQt5 import QtCore, QtGui, QtWidgets
from TableModels import SanObjTable
from DataBase import DataBase

class MyWindow(QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.Teams = []
        for i in range(1,10):
            self.widgetTeam = FormTeam(self.scrollAreaWidgetContentsTeams)
            self.widgetTeam.setObjectName('widgetTeam{}'.format(i))
            self.widgetTeam.setTeamNo('第{}队'.format(i))
            self.verticalLayoutTeams.addWidget(self.widgetTeam, 0, QtCore.Qt.AlignTop)
            self.Teams.append(self.widgetTeam)
        self.widgetHeros.labelItemsName.setText('武将库')
        self.widgetMagics.labelItemsName.setText('战法库')
        db = DataBase()
        headers, datas = db.exportHerosToTable()
        HeroTableModel = SanObjTable(headers,datas)
        self.widgetHeros.tableViewItems.setModel(HeroTableModel)

        headers, datas = db.exportMagicsToTable()
        MagicTableModel = SanObjTable(headers,datas)
        self.widgetMagics.tableViewItems.setModel(MagicTableModel)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    sys.exit(app.exec_())