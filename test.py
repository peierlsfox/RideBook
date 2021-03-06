import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from Ui.Ui_tryout import Ui_MainWindow
from PyQt5.QtCore import QStringListModel,QAbstractListModel,QModelIndex,QSize
from PyQt5.QtGui import QStandardItemModel,QStandardItem

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)

    def setupUi(self,MainWindow):
        super(MyWindow, self).setupUi(self)
        # self.widget = MyItem(self.scrollAreaWidgetContents)
        # self.widget_2= MyItem(self.scrollAreaWidgetContents)
        # for i in range(1,10):
        #     self.item1 = MyItem(self.scrollAreaWidgetContents)
        #     self.item1.setObjectName('item{}'.format(i))
        #     self.verticalLayout.addWidget(self.item1)

    def clickSuccess(self):
        print("Down!")


if __name__ == '__main__':  
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())