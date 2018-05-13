import sys

from PyQt5.QtWidgets import QApplication

# from management.gui.assets.style import load_style
from management.gui.form.__main_window__ import MainForm

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setStyleSheet(load_style())
    form = MainForm()
    form.show()
    app.setStyleSheet(open("style", 'r').read())

    sys.exit(app.exec_())
