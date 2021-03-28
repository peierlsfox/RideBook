from PyQt5.QtCore import QAbstractTableModel, QModelIndex, QVariant,Qt
from PyQt5.QtGui import QColor

HEADERS = ['武将','品阶','国家','自带战法']
BACKCOLORS = {'S':QColor(200,200,100),
            'A':QColor(200,100,200),
            'B':QColor(100,200,200),
            'C':QColor(100,100,200)}

class SanItemModel(QAbstractTableModel):
    
    def __init__(self, headers = HEADERS, datas = []) -> None:
        super().__init__()
        self.datas = datas
        self.headers = headers

    def data(self, index: QModelIndex, role: int):
        if (not index.isValid() or not (0 <= index.row() < len(self.datas))):
            return None
        row, col = index.row(), index.column()
        data = self.datas[row]
        #返回表格的内容
        if role == Qt.DisplayRole:
            item = data[col]
            return item
        #返回表格的对齐方式
        if role == Qt.TextAlignmentRole and 0 < col < self.columnCount(0)-1:
            return Qt.AlignCenter
        #设置品阶的背景色
        if role == Qt.BackgroundColorRole:
            item = data[col]
            if item == 'S' or item == 'A' or item == 'B' or item == 'C' :
                return BACKCOLORS[item]
        return None

    def rowCount(self, parent: QModelIndex) -> int:
        return len(self.datas)
    
    def columnCount(self, parent: QModelIndex) -> int:
        return len(self.headers)

    def headerData(self, section: int, orientation: Qt.Orientation, role: int):
        if role != Qt.DisplayRole:
            return None
        if orientation == Qt.Horizontal:
            return self.headers[section]
        return int(section +1)

    
    def flags(self, index):
        return Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsDragEnabled | Qt.ItemIsDropEnabled
    
    def supportedDropActions(self):
        return Qt.CopyAction | Qt.MoveAction

    def supportedDragActions(self):
        return Qt.CopyAction | Qt.MoveAction 