from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QDialog, QMessageBox

from management.core.database import ProjectsModel
from management.gui.form.generated.add_dialog import Ui_DialogAdd


class AddNewDialog(QDialog, Ui_DialogAdd):
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
