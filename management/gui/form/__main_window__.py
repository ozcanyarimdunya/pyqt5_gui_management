from PyQt5.QtCore import QEvent
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

        self.left_form.installEventFilter(self)
        self.middle_form.installEventFilter(self)

        self.initialise()
        self.configure()

    def initialise(self):
        splitter = QSplitter()
        self.left_form.setFrameShape(QFrame.StyledPanel)
        self.middle_form.setFrameShape(QFrame.StyledPanel)

        splitter.addWidget(self.left_form)
        splitter.addWidget(self.middle_form)
        splitter.setSizes([100, 400])

        self.gridLayout.addWidget(splitter)

    def configure(self):
        self.middle_form.bind_add_dialog(self.left_form.dialog)
        self.middle_form.bind_edit_dialog(self.middle_form.dialog)
        self.left_form.bind_add_dialog(self.left_form.dialog)
        self.left_form.bind_edit_dialog(self.middle_form.dialog)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Enter:
            if obj == self.left_form:
                self.statusbar.showMessage("Select project to go second window.")
            if obj == self.middle_form:
                self.statusbar.showMessage("Select project to edit, delete or configure.")
        return super().eventFilter(obj, event)
