from PyQt5.QtCore import QModelIndex, pyqtSlot
from PyQt5.QtWidgets import QFrame, QAbstractItemView, QTableView, QMessageBox

from management.core.database import ProjectsModel
from management.core.table_models import CustomTableModel
from management.gui.form.add_dialog import AddNewDialog
from management.gui.form.edit_dialog import EditDialog
from management.gui.form.generated.middle import Ui_FormMiddle


class MiddleWidget(QFrame, Ui_FormMiddle):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.initialise()
        self.configure()

    def initialise(self):
        self.tableViewData.setSelectionBehavior(QTableView.SelectRows)
        self.tableViewData.setSelectionMode(QAbstractItemView.SingleSelection)
        self.fill_table()

        # Need to define in here first
        self.dialog = EditDialog(project_id=None)

    def configure(self):
        self.tableViewData.doubleClicked.connect(lambda row_item: self.table_cell_double_clicked(row_item))
        self.pushButton_Configure.clicked.connect(lambda: self.push_button_configure_clicked())
        self.pushButton_Edit_Delete.clicked.connect(lambda: self.push_button_edit_delete_clicked())

    @pyqtSlot()
    def fill_table(self):
        self.tableViewData.clearSpans()
        header, data = ProjectsModel().get_projects()
        model = CustomTableModel(header=header, data=data)
        self.tableViewData.setModel(model)

    def bind_add_dialog(self, dialog: AddNewDialog):
        dialog.onAddButtonClicked.connect(lambda: self.fill_table())

    def bind_edit_dialog(self, dialog: EditDialog):
        dialog.onSaveButtonClicked.connect(lambda: self.fill_table())

    def table_cell_double_clicked(self, row_item: QModelIndex):
        _id = row_item.model().index(row_item.row(), 0).data()
        QMessageBox.information(self, "Information", "Selected items data: " + str(_id))

        # open second window

    def push_button_configure_clicked(self):
        if not len(self.tableViewData.selectedIndexes()) > 0:
            return

        row_item = self.tableViewData.selectedIndexes()[0]
        _id = row_item.model().index(row_item.row(), 0).data()

        # switch configuration page

    def push_button_edit_delete_clicked(self):
        if not len(self.tableViewData.selectedIndexes()) > 0:
            return

        row_item = self.tableViewData.selectedIndexes()[0]
        _id = row_item.model().index(row_item.row(), 0).data()

        self.dialog.project_id = _id
        # need to re-initialise to update project_id
        self.dialog.initialise()
        self.dialog.show()
