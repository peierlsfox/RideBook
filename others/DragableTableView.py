from PyQt5.QtCore import Qt,QMimeData,QModelIndex
from PyQt5.QtWidgets import QTableView
from PyQt5 import QtGui
from PyQt5.QtGui import QColor, QDrag, QPainter, QPixmap

class DragableTableView(QTableView):
    def __init__(self,parent=None):
        super().__init__(parent)

    def mouseMoveEvent(self, e: QtGui.QMouseEvent) -> None:
        if e.buttons() != Qt.LeftButton:
            return None
        #根据currentIndex获取数据行的名称
        mimeData = QMimeData()
        currentRow = self.currentIndex().row()
        index = self.model().index(currentRow,0)
        itemName = self.model().data(index)
        mimeData.setText(itemName)
        
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
        return super().mouseMoveEvent(e)