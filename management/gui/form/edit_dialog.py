from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QDialog, QMessageBox

from management.core.database import ProjectsModel
from management.gui.form.generated.edit_dialog import Ui_DialogEdit


class EditDialog(QDialog, Ui_DialogEdit):
    onSaveButtonClicked = pyqtSignal()

    def __init__(self, project_id):
        super().__init__()
        self.setupUi(self)

        self.project_id = project_id
        self.old_project_name = None
        self.old_company_name = None

        self.initialise()
        self.configure()

    def initialise(self):
        # First initialising require to bind event, so _id is None
        if not self.project_id:
            return
        prj = ProjectsModel().get_project(_id=self.project_id)
        self.old_project_name = str(prj[1])
        self.old_company_name = str(prj[2])
        self.lineEdit_ProjectName.setText(self.old_project_name)
        self.lineEdit_CompanyName.setText(self.old_company_name)

    def clear_form(self):
        self.lineEdit_ProjectName.clear()
        self.lineEdit_CompanyName.clear()

    def configure(self):
        self.setModal(True)
        self.pushButton_OK.clicked.connect(lambda: self.btn_ok_clicked())  # outline function
        self.pushButton_Cancel.clicked.connect(lambda: self.close())  # inline function
        self.pushButton_Delete.clicked.connect(lambda: self.btn_delete_clicked())

    def btn_ok_clicked(self):
        project_name: str = self.lineEdit_ProjectName.text()
        company_name: str = self.lineEdit_CompanyName.text()

        if (not project_name.strip()) or (not company_name.strip()):
            QMessageBox.warning(self, "Information", "Please specify project and company name!")
            return

        if (project_name != self.old_project_name) or (company_name != self.old_company_name):
            ProjectsModel().update_project(_id=self.project_id, name=project_name, company=company_name)

        # Notify that if our project is updated in database
        # So that middle form refresh its table
        self.onSaveButtonClicked.emit()
        self.close()

    def btn_delete_clicked(self):
        result = QMessageBox.question(self, "Delete project", "Delete project ?", QMessageBox.Yes | QMessageBox.No)
        if result == QMessageBox.Yes:
            ProjectsModel().delete_project(_id=self.project_id)
            self.onSaveButtonClicked.emit()
            self.close()
        else:
            ...
