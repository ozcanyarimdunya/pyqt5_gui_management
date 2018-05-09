import os
import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtWebKitWidgets import QWebView
from PyQt5.QtWidgets import QApplication


class Browser(QWebView):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 150, 800, 500)
        self.setWindowTitle('Loading...')
        self.titleChanged.connect(lambda: self.setWindowTitle(self.title()))

        self.load(QUrl.fromLocalFile(os.path.abspath("local.html")))


app = QApplication(sys.argv)
view = Browser()
view.show()
app.exec_()
