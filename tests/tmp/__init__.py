# https://gist.github.com/Riateche/5984815
import sip

from PyQt5.QtCore import QAbstractTableModel, QModelIndex, Qt, pyqtSlot
from PyQt5.QtWidgets import QItemDelegate, QPushButton, QComboBox, QTableView, QWidget, QVBoxLayout, QApplication, \
    QHBoxLayout, QGroupBox, QFrame

sip.setapi('QString', 2)
sip.setapi('QVariant', 2)


class TableModel(QAbstractTableModel):
    def rowCount(self, parent=QModelIndex()):
        return 2

    def columnCount(self, parent=QModelIndex()):
        return 2

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None
        if not role == Qt.DisplayRole:
            return None

        return "{0:02d}".format(index.row())

    def setData(self, index, value, role=Qt.DisplayRole):
        print("setData", index.row(), index.column(), value)

    def flags(self, index):
        if index.column() == 0:
            return Qt.ItemIsSelectable | Qt.ItemIsEnabled
        else:
            return Qt.ItemIsEnabled


class ButtonDelegate(QItemDelegate):

    def __init__(self, parent):
        super().__init__(parent)

    def createEditor(self, parent, option, index):
        frame = QWidget(parent)
        box = QHBoxLayout(frame)
        btn_1 = QPushButton("Edit")
        btn_2 = QPushButton("Update")
        box.addWidget(btn_1)
        box.addWidget(btn_2)
        box.setContentsMargins(0, 0, 0, 0)
        frame.setLayout(box)
        frame.setContentsMargins(0, 0, 0, 0)

        return frame


class TableView(QTableView):
    """
    A simple table to demonstrate the QComboBox delegate.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setItemDelegateForColumn(0, ButtonDelegate(self))


class Widget(QWidget):
    """
    A simple test widget to contain and own the model and table.
    """

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        l = QVBoxLayout(self)
        self._tm = TableModel(self)
        self._tv = TableView(self)

        self._tv.setShowGrid(False)
        self._tv.setAlternatingRowColors(True)
        self._tv.setModel(self._tm)
        for row in range(0, self._tm.rowCount()):
            # self._tv.openPersistentEditor(self._tm.index(row, 0))
            self._tv.openPersistentEditor(self._tm.index(row, 0))

        l.addWidget(self._tv)
        self.setLayout(l)


if __name__ == "__main__":
    from sys import argv, exit

    a = QApplication(argv)
    w = Widget()
    w.move(200, 100)
    w.resize(400, 300)
    w.show()
    w.raise_()
    exit(a.exec_())
