import sys
import time

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QWidget, QApplication

from tests.tmp.multi_thread import Ui_FormMultiThread


class GenericThread(QThread):
    onStarted = pyqtSignal()
    onFinished = pyqtSignal()
    onValueChanged = pyqtSignal(int)

    def __init__(self, _range: range, _sleep: float):
        print("[GenericThread]:Thread initialised:")
        super().__init__()

        print("[GenericThread]:Thread args set:")
        self._range = _range
        self._sleep = _sleep

    def run(self):
        print("[GenericThread]:Thread started:")
        self.onStarted.emit()

        print("[GenericThread]:Thread running:")
        for val in self._range:
            time.sleep(self._sleep)
            self.onValueChanged.emit(val)

        print("[GenericThread]:Thread finished:")
        self.onFinished.emit()


class MultiThreadForm(QWidget, Ui_FormMultiThread):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.move(550, 300)
        self.configure()

    def configure(self):
        self.pushButton_start_1.clicked.connect(lambda: self.pushButton_start_1_clicked())
        self.pushButton_start_2.clicked.connect(lambda: self.pushButton_start_2_clicked())
        self.pushButton_set.clicked.connect(lambda: self.pushButton_set_clicked())

    def pushButton_start_1_clicked(self):
        def change_state(state):
            self.pushButton_start_1.setEnabled(state)

        def change_pb_value(val):
            self.progressBar_1.setValue(val)

        self.thread_1 = GenericThread(_range=range(101), _sleep=0.1)
        self.thread_1.start()

        self.thread_1.onStarted.connect(lambda: change_state(False))
        self.thread_1.onFinished.connect(lambda: change_state(True))
        self.thread_1.onValueChanged.connect(lambda val: change_pb_value(val))

    def pushButton_start_2_clicked(self):
        def change_state(state):
            self.pushButton_start_2.setEnabled(state)

        def change_pb_value(val):
            self.progressBar_2.setValue(val)

        self.thread_1 = GenericThread(_range=range(101), _sleep=0.2)
        self.thread_1.start()

        self.thread_1.onStarted.connect(lambda: change_state(False))
        self.thread_1.onFinished.connect(lambda: change_state(True))
        self.thread_1.onValueChanged.connect(lambda val: change_pb_value(val))

    def pushButton_set_clicked(self):
        ...


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MultiThreadForm()
    form.show()
    sys.exit(app.exec_())
