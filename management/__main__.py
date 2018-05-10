import sys

from PyQt5.QtWidgets import QApplication

from management.gui.form.__main_window__ import MainForm

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainForm()
    form.show()
    sys.exit(app.exec_())
