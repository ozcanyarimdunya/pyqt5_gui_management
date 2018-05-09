from PyQt5.QtWidgets import QMainWindow, QSplitter, QFrame

from management.gui.form.generated.main import Ui_MainWindow
from management.gui.form.left_widget import LeftWidget
from management.gui.form.middle_widget import MiddleWidget


class MainForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.move(300, 100)

        self.middle_form = MiddleWidget(parent=self)
        self.left_form = LeftWidget(parent=self)

        self.initialise()
        self.configure()

    def initialise(self):
        splitter = QSplitter()
        self.left_form.setFrameShape(QFrame.StyledPanel)
        self.middle_form.setFrameShape(QFrame.StyledPanel)

        splitter.addWidget(self.left_form)
        splitter.addWidget(self.middle_form)

        self.gridLayout.addWidget(splitter)

    def configure(self):
        self.middle_form.bind_add_dialog(self.left_form.dialog)
        self.middle_form.bind_edit_dialog(self.middle_form.dialog)
