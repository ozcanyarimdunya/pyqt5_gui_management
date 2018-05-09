from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QFrame, QAbstractItemView, QTableView

from management.core.database import ProjectsModel
from management.core.table_models import CustomListModel
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

    def configure(self):
        # Need to define in here first
        self.dialog = EditDialog(project_id=None)
        self.tableViewData.doubleClicked.connect(lambda row_item: self.table_cell_double_clicked(row_item))

    def fill_table(self):
        header, data = ProjectsModel().get_projects()
        model = CustomListModel(header=header, data=data)
        self.tableViewData.setModel(model)

    def table_cell_double_clicked(self, row_item):
        _id = 0
        for index in self.tableViewData.selectedIndexes():
            model: CustomListModel = index.model()
            for column in range(model.columnCount()):
                index = model.index(row_item.row(), column)
                _id = (model.data(index)).value()
                break  # _id is in first place

        self.dialog.project_id = _id
        self.dialog.initialise()
        self.dialog.show()

    def bind_add_dialog(self, dialog: AddNewDialog):
        dialog.onAddButtonClicked.connect(lambda: self.refresh_table())

    def bind_edit_dialog(self, dialog: EditDialog):
        dialog.onSaveButtonClicked.connect(lambda: self.refresh_table())

    @pyqtSlot()
    def refresh_table(self):
        try:
            self.tableViewData.clearSpans()
        except Exception as e:
            print(f'Error: {e}')
        self.fill_table()
