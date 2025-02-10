# PyQt5 Basic GUI boiler plate code

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon 

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GUI Window")
        self.setGeometry(500, 200, 500, 500)       # setGeometry(x, y, width, height)
                 

if __name__ == "__main__":
    app = QApplication(sys.argv)                    
    window = MainWindow()     
    window.show()                     
    sys.exit(app.exec_()) 