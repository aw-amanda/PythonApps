# PyQt5 Radio buttons
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QButtonGroup

# With the default behavior of PyQt5, all radio buttons, unless explicitly stated, are part of the same group
# By default, only one radio button can be selected; separating them into groups will allow more than one radio button selection per page, but still only one per group 


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.radio1 = QRadioButton("Visa", self)    # self arg adds the radio button directly to the window
        self.radio2 = QRadioButton("MasterCard", self)
        self.radio3 = QRadioButton("PayPal", self)
        self.radio4 = QRadioButton("In-store", self)
        self.radio5 = QRadioButton("Online", self)

        self.button_group1 = QButtonGroup(self)
        self.button_group2 = QButtonGroup(self)

        self.initUI()

    def initUI(self):
        self.radio1.setGeometry(20, 0, 300, 50)
        self.radio2.setGeometry(20, 100, 350, 50) # MasterCard is longer word and needs a longer width
        self.radio3.setGeometry(20, 200, 300, 50)
        self.radio4.setGeometry(20, 300, 300, 50)
        self.radio5.setGeometry(20, 400, 300, 50)

        self.setStyleSheet("QRadioButton{"          # QRadioButton selector + {} applies CSS style to entire widget group)
                           "font-size: 40px;"
                           "font-family: Arial;"
                           "padding: 50px;""}")
        
        # Group radio buttons into separate groups:
        self.button_group1.addButton(self.radio1)
        self.button_group1.addButton(self.radio2)
        self.button_group1.addButton(self.radio3)
        self.button_group2.addButton(self.radio4)
        self.button_group2.addButton(self.radio5)

        # Use a signal to toggle the radio buttons by connecting a signal to a slot
        self.radio1.toggled.connect(self.radio_button_changed)
        self.radio2.toggled.connect(self.radio_button_changed)
        self.radio3.toggled.connect(self.radio_button_changed)
        self.radio4.toggled.connect(self.radio_button_changed)
        self.radio5.toggled.connect(self.radio_button_changed)

    def radio_button_changed(self):
        radio_button = self.sender()    # inputs whichever radio button above is sending the message (was selected)
        if radio_button.isChecked():
            print(f"{radio_button.text()} is selected.")




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())