from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel, QTableView
from PyQt5.QtGui import QColor, QDrag, QPainter, QPixmap
from PyQt5.QtCore import QModelIndex, QRect, Qt, QMimeData
from PyQt5 import QtGui


#可拖拽的QLabel
class DropableLabel(QLabel):

    def __init__(self,parent = None,type = 'hero', address = ''):
        super().__init__(parent)
        self.setType(type)
        self.setAddress(address)
        self.setAcceptDrops(True)
    
    def mouseMoveEvent(self, ev):
        if ev.buttons() != Qt.LeftButton:
            return
        #拖拽包含的数据
        mimeData = QMimeData()
        mimeData.setText('{}:{}:{}'.format(self.type,self.address,self.text()))
        drag = QDrag(self)
        drag.setMimeData(mimeData)
        #拖拽物体的图标通过抓取自身的图像获得
        pixmap = QPixmap(self.size())
        painter = QPainter(pixmap)
        painter.drawPixmap(self.rect(), self.grab())
        painter.end()
        drag.setPixmap(pixmap)
        drag.setHotSpot(ev.pos()-self.rect().topLeft())
        drag.exec_(Qt.MoveAction)

    def dragEnterEvent(self, ev:QtGui.QDropEvent):
        txt = ev.mimeData().text()
        type,address,content = txt.split(':')
        if type == self.type:
            ev.accept()

    def dropEvent(self, ev:QtGui.QDropEvent):
        # pos = ev.pos()
        # ev.setDropAction(Qt.MoveAction)
        print(ev.mimeData().text(),end='->')
        print('{}:{}:{}'.format(self.type,self.address,self.text()))
        # self.setText(ev.mimeData().text())
        # ev.accept()

    def setType(self, type):
        self.type = type
    def setAddress(self, addr):
        self.address = addr

class DragableTableView(QTableView):
    def __init__(self, parent = None, type = 'hero'):
        super().__init__(parent)
        self.setType(type)
        
    def mouseMoveEvent(self, e: QtGui.QMouseEvent) -> None:
        if e.buttons() != Qt.LeftButton:
            return
        #把所选择的行的第一列的名称作为拖拽传递的数据
        row = self.currentIndex().row()
        text = self.model().index(row,0).data()
        #设置拖拽的图标
        width = self.columnWidth(0)
        height = self.rowHeight(row)
        pixmap = QPixmap(width,height)
        painter = QPainter(pixmap)
        painter.begin(self)
        painter.fillRect(pixmap.rect(),QColor(230,230,230))
        painter.drawRect(0,0,width-1,height-1)
        painter.drawText(pixmap.rect(),Qt.AlignCenter,text)
        painter.end()

        mimeData = QMimeData()
        mimeData.setText('{}:{}:{}'.format(self.type,self.objectName(),text))
        drag = QDrag(self)
        drag.setMimeData(mimeData)
        drag.setPixmap(pixmap)
        drag.exec_(Qt.MoveAction)
        return super().mouseMoveEvent(e)

    def setType(self, type):
        self.type = type
