from PyQt5.QtWidgets import QFrame

from management.gui.form.add_dialog import AddNewDialog
from management.gui.form.generated.left import Ui_FormLeft


class LeftWidget(QFrame, Ui_FormLeft):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.initialise()
        self.configure()

    def initialise(self):
        pass

    def configure(self):
        # Need to define in here first
        self.dialog = AddNewDialog()
        self.pushButton_CreateNewProject.clicked.connect(lambda: self.btn_create_clicked())

    def btn_create_clicked(self):
        self.dialog.show()
