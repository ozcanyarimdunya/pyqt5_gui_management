import sys
from abc import abstractmethod
from enum import Enum

from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QMainWindow

from management.gui.form import *

DIALOG_STATE = {}


class Dialog(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initialise()

    def initialise(self):
        self.setModal(True)
        self.pushButton_OK.clicked.connect(lambda: self.btn_ok_clicked())  # outline function
        self.pushButton_Cancel.clicked.connect(lambda: self.close())  # inline function

        self.lineEdit_ProjectName.setText("Demo Project")
        self.lineEdit_CompanyName.setText("Demo Company")

    def btn_ok_clicked(self):
        project_name = self.lineEdit_ProjectName.text()
        company_name = self.lineEdit_CompanyName.text()
        DIALOG_STATE.__setitem__(self.DialogType.DIALOG_TYPE_PROJECT_NAME, project_name)
        DIALOG_STATE.__setitem__(self.DialogType.DIALOG_TYPE_COMPANY_NAME, company_name)

        for st in self.DialogType:
            if DIALOG_STATE.get(st):
                print(DIALOG_STATE.get(st))

    class DialogType(Enum):
        DIALOG_TYPE_PROJECT_NAME = "Project Name"
        DIALOG_TYPE_COMPANY_NAME = "Company Name"


class BaseForm(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.initialise()

    @abstractmethod
    def initialise(self): ...


class LeftForm(BaseForm, Ui_FormLeft):

    def initialise(self):
        self.pushButton_CreateNewProject.clicked.connect(lambda: self.btn_create_clicked())

    @staticmethod
    def btn_create_clicked():
        dialog = Dialog()
        dialog.show()


class MiddleForm(BaseForm, Ui_FormMiddle):

    def initialise(self):
        pass


class MainForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initialise()

    def initialise(self):
        self.left_form = LeftForm(parent=self)
        self.gridLayout.addWidget(self.left_form, 0, 0, 1, 1)
        self.middle_form = MiddleForm(parent=self)
        self.gridLayout.addWidget(self.middle_form, 0, 1, 1, 1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainForm()
    form.show()
    sys.exit(app.exec_())
