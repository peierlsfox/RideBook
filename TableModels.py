from PyQt5.QtCore import QAbstractTableModel,QModelIndex,QVariant,Qt
from PyQt5.QtGui import QColor
from DataBase import DataBase
from Models import Hero

class SanObjTable(QAbstractTableModel):
    def __init__(self, headers = [], datas = []) -> None:
        super().__init__()
        self.datas = datas
        self.headers = headers
    # 必须实现的接口方法（返回数据行数）
    def rowCount(self,index=QModelIndex()):           
        return len(self.datas)

    # 必须实现的接口方法（返回数据列数）
    def columnCount(self,index=QModelIndex()):        
        return len(self.headers)    

    def headerData(self,section,orientation,role=Qt.DisplayRole):
        # 实现标题行的定义
        if role != Qt.DisplayRole:
            return None
 
        if orientation == Qt.Horizontal:
            return self.headers[section]
        return int(section + 1)

    def data(self,index,role=Qt.DisplayRole):
        # 供视图调用，以获取用以显示的数据
        if (not index.isValid() or not (0 <= index.row() < len(self.datas))):  # 无效的数据请求
            return None
 
        row,col = index.row(),index.column()
        data = self.datas[row]
        if role == Qt.DisplayRole:
            item = data[col]
            return item
        if role == Qt.TextAlignmentRole and col > 0 :
            return Qt.AlignCenter
        if role == Qt.BackgroundColorRole:
            item = data[col]
            if item == 'S':
                return QColor(250,250,100)
            if item == 'A':
                return QColor(200,100,200)
            if item == 'B':
                return QColor(100,200,200)
            if item == 'C':
                return QColor(100,200,100)
            return None
        return None

    def load(self):
        self.beginResetModel()
        db = DataBase()
        index = 0
        for hero in db.heros:
            index += 1
            self.datas.append([hero.name,hero.grade,hero.group,hero.magicSelf.name])
        self.endResetModel

    def flags(self, index):  # 必须实现的接口方法，不实现，则View中数据不可编辑
        if not index.isValid():
            return Qt.ItemIsEnabled
        return Qt.ItemFlags(
                QAbstractTableModel.flags(self, index)|
                Qt.ItemIsEditable | Qt.ItemIsSelectable | Qt.ItemIsDropEnabled | Qt.ItemIsDragEnabled)