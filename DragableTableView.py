from PyQt5.QtCore import QAbstractItemModel, QAbstractTableModel, Qt,QMimeData,QModelIndex
from PyQt5.QtWidgets import QAbstractItemView, QTableView
from PyQt5 import QtGui
from PyQt5.QtGui import QColor, QDrag, QPainter, QPixmap
from SanHelp import SanHelp

class DragableTableView(QTableView):
    def __init__(self,parent=None,type = SanHelp.HeroType, addr = 'Lib'):
        super().__init__(parent)
        self.type = type
        self.address = addr
        self.setAcceptDrops(True)
        self.setDropIndicatorShown(True)
        # self.setDragDropOverwriteMode(False)
        self.setDragDropMode(QAbstractItemView.DragDrop)

    def mouseMoveEvent(self, e: QtGui.QMouseEvent) -> None:
        if e.buttons() != Qt.LeftButton:
            return None
        #根据currentIndex获取数据行的名称
        mimeData = QMimeData()
        currentRow = self.currentIndex().row()
        index = self.model().index(currentRow,0)
        itemName = self.model().data(index)
        mimeData.setText('{}:{}:{}'.format(self.type,self.address,itemName))
        
        #绘制拖动时的图像
        width = self.columnWidth(0)
        height = self.rowHeight(currentRow)
        pixmap = QPixmap(width,height)
        paint = QPainter()
        paint.begin(pixmap)
        paint.fillRect(pixmap.rect(),QColor(Qt.white))
        paint.drawRect(0,0,width-1,height-1)
        paint.drawText(pixmap.rect(),Qt.AlignCenter,itemName)
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
        self.setFrameShape(2)

    def dragMoveEvent(self, e: QtGui.QDragMoveEvent) -> None:
        txt = e.mimeData().text()
        type, addr, content = txt.split(':')
        if type == self.type:
            e.accept()

    def dropEvent(self, e: QtGui.QDropEvent) -> None:
        txt = e.mimeData().text()
        type, addr, content = txt.split(':')
        print('drop from {}:{} to {}'.format(addr,content,self.address))
        self.setFrameStyle(2)

    def setAddress(self, addr):
        self.address = addr

    def setType(self, type):
        self.type = type
