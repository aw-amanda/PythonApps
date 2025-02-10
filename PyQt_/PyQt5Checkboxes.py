# Checkboxes with PyQt5

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox
from PyQt5.QtCore import Qt 


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.checkbox = QCheckBox("Check1", self) 
        self.initUI()

    def initUI(self):
        self.checkbox.setGeometry(10, 0, 500, 100)
        self.checkbox.setStyleSheet("font-size: 30px;"
                                    "font-family: Arial;")
        # default unchecked; to set to be checked when the window loads:
        #self.checkbox.setChecked(True)
        self.checkbox.setChecked(False)

        self.checkbox.stateChanged.connect(self.checkbox_changed)
    
    def checkbox_changed(self, state):  # state parameter is provided after interacting with checkbox
        if state == Qt.Checked:
            print("Checked")
        else:
            print("Not checked")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())