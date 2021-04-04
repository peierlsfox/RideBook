from PyQt5.QtCore import Qt,QMimeData
from PyQt5.QtWidgets import QLabel
from PyQt5 import QtGui
from PyQt5.QtGui import QColor, QDrag, QPainter, QPixmap
from SanHelp import SanHelp
from Server import Server

class DragableLabel(QLabel):
    def __init__(self,parent = None,type = SanHelp.HeroType):
        super().__init__(parent)        
        self.setAcceptDrops(True)
        self.setType(type)
        self.server = Server()

    def mouseMoveEvent(self, e: QtGui.QMouseEvent) -> None:
        if e.buttons() != Qt.LeftButton:
            return None
        #根据currentIndex获取数据行的名称
        mimeData = QMimeData()
        mimeData.setText('{}:{}:{}'.format(self.type,self.address,self.text()))
        
        #绘制拖动时的图像
        pixmap = QPixmap(self.size())
        
        paint = QPainter()
        paint.begin(pixmap)
        # paint.fillRect(pixmap.rect(),QColor(Qt.white))
        # paint.drawRect(pixmap.rect())
        paint.drawPixmap(self.rect(),self.grab())
        paint.drawText(pixmap.rect(),Qt.AlignCenter,self.text())
        paint.end()

        #设定拖动项的数据和图标
        drag = QDrag(self)
        drag.setMimeData(mimeData)
        drag.setPixmap(pixmap)
        drag.exec_(Qt.MoveAction)
        super().mouseMoveEvent(e)
        

    def dragEnterEvent(self, e: QtGui.QDragEnterEvent):
        txt = e.mimeData().text()
        type, addr, content = txt.split(':')
        if type == self.type:
            e.accept()
            self.setFrameStyle(3)
    
    def dragLeaveEvent(self, e: QtGui.QDragLeaveEvent) -> None:
        self.setFrameShape(1)

    def dragMoveEvent(self, e: QtGui.QDragMoveEvent) -> None:
        txt = e.mimeData().text()
        type, addr, content = txt.split(':')
        if type == self.type:
            e.accept()

    def dropEvent(self, e: QtGui.QDropEvent) -> None:
        txt = e.mimeData().text()
        type, addr, content = txt.split(':')
        if self.server:
            self.server.change(type,addr,content,self.address,self.text())
        # print('drop from {}:{} to {}'.format(addr,content,self.address))
        self.setFrameStyle(1)

    def setAddress(self, addr):
        self.address = addr

    def setType(self, type):
        self.type = type

    def setServer(self, server:Server):
        self.server = server