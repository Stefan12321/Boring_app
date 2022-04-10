import random

from main_window import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt


class Boring(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        self.close_ = False
        QtWidgets.QMainWindow.__init__(self, parent=parent)
        self.setupUi(self)
        self.checkbox_dict = [self.checkBox_1, self.checkBox_2, self.checkBox_3, self.checkBox_4,
                         self.checkBox_5, self.checkBox_6, self.checkBox_7, self.checkBox_8,]
        self.add_functions()

    def add_functions(self):
        for checkbox in self.checkbox_dict:
            checkbox.stateChanged.connect(self.random_bug)

    def random_bug(self):
        for checkbox in self.checkbox_dict:
            checkbox.stateChanged.disconnect()
        for i in range(0, random.randint(1, 6)):
            checkbox = random.choice(self.checkbox_dict)
            if self.sender() != checkbox:
                if checkbox.isChecked():
                    checkbox.setCheckState(Qt.CheckState.Unchecked)
                else:
                    checkbox.setCheckState(Qt.CheckState.Checked)
            else:
                i -= 1
        self.add_functions()


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = Boring()
    w.show()
    sys.exit(app.exec_())
