import sys
from abc import abstractmethod

from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QModelIndex
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QSplitter, QFrame, QMessageBox, QAbstractItemView, \
    QTableView

from management.core.database import ProjectsModel
from management.core.table_models import CustomListModel
from management.gui.form import *

CREATE_PROJECT = 0
UPDATE_PROJECT = 1


class BaseForm(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.initialise()
        self.configure()

    @abstractmethod
    def initialise(self): ...

    def configure(self): ...


class AddNewDialog(QDialog, Ui_Dialog):
    onAddButtonClicked = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initialise()
        self.configure()

    def initialise(self):
        self.clear_form()

    def clear_form(self):
        self.lineEdit_ProjectName.clear()
        self.lineEdit_CompanyName.clear()

    def configure(self):
        self.setModal(True)
        self.pushButton_OK.clicked.connect(lambda: self.btn_ok_clicked())  # outline function
        self.pushButton_Cancel.clicked.connect(lambda: self.close())  # inline function

    def btn_ok_clicked(self):
        project_name: str = self.lineEdit_ProjectName.text()
        company_name: str = self.lineEdit_CompanyName.text()

        if (not project_name.strip()) or (not company_name.strip()):
            QMessageBox.warning(self, "Information", "Please specify project and company name!")
            return

        # Database interaction
        ProjectsModel().add_project(name=project_name, company=company_name)

        # Notify that our project is added to database
        # So that middle form refresh its table
        self.onAddButtonClicked.emit()

        self.clear_form()
        self.close()


class EditDialog(QDialog, Ui_Dialog):
    onEditClicked = pyqtSignal()

    def __init__(self, _id):
        super().__init__()
        self.setupUi(self)

        self._id = _id
        self.initialise()
        self.configure()

    def initialise(self):
        prj = ProjectsModel().get_project(_id=self._id)
        self.lineEdit_ProjectName.setText(str(prj[1]))
        self.lineEdit_CompanyName.setText(str(prj[2]))

        self.pushButton_OK.setText("Save")

    def clear_form(self):
        self.lineEdit_ProjectName.clear()
        self.lineEdit_CompanyName.clear()

    def configure(self):
        self.setModal(True)
        self.pushButton_OK.clicked.connect(lambda: self.btn_ok_clicked())  # outline function
        self.pushButton_Cancel.clicked.connect(lambda: self.close())  # inline function

    def btn_ok_clicked(self):
        project_name: str = self.lineEdit_ProjectName.text()
        company_name: str = self.lineEdit_CompanyName.text()

        if (not project_name.strip()) or (not company_name.strip()):
            QMessageBox.warning(self, "Information", "Please specify project and company name!")
            return

        # Database interaction
        ProjectsModel().update_project(_id=self._id, name=project_name, company=company_name)

        # Notify that our project is updated in database
        # So that middle form refresh its table
        # self.onEditClicked.emit()

        self.clear_form()
        self.close()


class LeftForm(BaseForm, Ui_FormLeft):

    def initialise(self):
        # Need to define in here first
        self.dialog = AddNewDialog()
        self.pushButton_CreateNewProject.clicked.connect(lambda: self.btn_create_clicked())

    def btn_create_clicked(self):
        self.dialog.attr.__setitem__("flag", CREATE_PROJECT)
        self.dialog.show()


class MiddleForm(BaseForm, Ui_FormMiddle):
    def initialise(self):

        # self.tableViewData.setSelectionBehavior(QTableView.SelectRows)
        self.tableViewData.setSelectionMode(QAbstractItemView.SingleSelection)
        self.fill_table()

    def configure(self):
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

        self.dialog = EditDialog(_id=_id)
        self.dialog.show()

    def connect_dialog_click_event(self, dialog: AddNewDialog):
        dialog.onAddButtonClicked.connect(lambda: self.refresh_table())

    @pyqtSlot()
    def refresh_table(self):
        try:
            self.tableViewData.clearSpans()
        except Exception as e:
            print(f'Error: {e}')
        self.fill_table()


class MainForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initialise()
        self.configure()

    def initialise(self):
        splitter = QSplitter()
        self.left_form = LeftForm(parent=self)
        self.left_form.setFrameShape(QFrame.StyledPanel)

        self.middle_form = MiddleForm(parent=self)
        self.middle_form.setFrameShape(QFrame.StyledPanel)

        splitter.addWidget(self.left_form)
        splitter.addWidget(self.middle_form)

        self.gridLayout.addWidget(splitter)

    def configure(self):
        self.middle_form.connect_dialog_click_event(self.left_form.dialog)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainForm()
    form.show()
    sys.exit(app.exec_())
