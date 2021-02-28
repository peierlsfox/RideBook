from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel
from PyQt5.QtGui import QDrag, QPainter, QPixmap
from PyQt5.QtCore import Qt, QMimeData
from PyQt5 import QtGui


#可拖拽的QLabel
class DropableLabel(QLabel):
    def __init__(self,parent = None,type = ''):
        super().__init__(parent)
        self.type = type
        self.setAcceptDrops(True)
    
    def mouseMoveEvent(self, ev):
        if ev.buttons() != Qt.LeftButton:
            return
        #拖拽包含的数据
        mimeData = QMimeData()
        mimeData.setText('{}:{}'.format(self.text(),self.objectName()))
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

    def dragEnterEvent(self, ev):
        ev.accept()

    def dropEvent(self, ev:QtGui.QDropEvent):
        # pos = ev.pos()
        # ev.setDropAction(Qt.MoveAction)
        self.setText(ev.mimeData().text())
        # ev.accept()

    