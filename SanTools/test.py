from FormMember import FormMember
from FormTeam import FormTeam
from os import name
from DataBase import DataBase
from Models import Magic, Hero, Book
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow

db = DataBase()
# for magic in db.magics:
#     print('{}:{}'.format(magic.name,magic.grade))
# for hero in db.heros:
#     print('{}:{}'.format(hero.name,hero.grade))

app = QApplication(sys.argv)
mainWindow = QMainWindow()
ui = FormTeam(mainWindow)
mainWindow.show()
sys.exit(app.exec_())

