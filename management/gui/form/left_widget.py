from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QFrame, QMessageBox

from management.core.database import ProjectsModel
from management.gui.form.add_dialog import AddNewDialog
from management.gui.form.edit_dialog import EditDialog
from management.gui.form.generated.left import Ui_FormLeft


class LeftWidget(QFrame, Ui_FormLeft):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.initialise()
        self.configure()

    def initialise(self):
        self.fill_projects_list()
        # Need to define in here first
        self.dialog = AddNewDialog()

    def configure(self):
        self.pushButton_CreateNewProject.clicked.connect(lambda: self.btn_create_clicked())
        self.listView.doubleClicked.connect(lambda index: self.list_view_double_clicked(index))

    def bind_add_dialog(self, dialog: AddNewDialog):
        dialog.onAddButtonClicked.connect(lambda: self.fill_projects_list())

    def bind_edit_dialog(self, dialog: EditDialog):
        dialog.onSaveButtonClicked.connect(lambda: self.fill_projects_list())

    @pyqtSlot()
    def fill_projects_list(self):
        header, data = ProjectsModel().get_projects()
        model = QStandardItemModel(parent=self.listView)
        model.removeRows(0, model.rowCount())
        for project in data:
            item = QStandardItem(project[1])
            item.setEditable(False)

            model.appendRow(item)
        self.listView.setModel(model)

    def list_view_double_clicked(self, row_item):
        _data = row_item.model().index(row_item.row(), 0).data()
        QMessageBox.information(self, "Information", "Selected items data: " + str(_data))

    def btn_create_clicked(self):
        self.dialog.show()
