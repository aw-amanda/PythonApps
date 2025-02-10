# Boiler plate code for PyQt5 Applications

import sys

from PyQt5.QtCore import *              # Core non-GUI functionality (events, signals, slots, I/O, threads, data types, etc.)
from PyQt5.QtGui import *               # GUI elements (windows, dialogs, buttons, layouts, fonts)
from PyQt5.QtWidgets import *           # UI elements (widgets for displaying data, input fields, complex layouts, etc.)
from PyQt5.QtMultimedia import *        # Classes for handling audio, video, cameras, radio functionality
from PyQt5.QtNetwork import *           # Functionality for network programming; TCP/IP, UDP, HTTP, etc.
from PyQt5.QtPrintSupport import *      # Classes for printing and print preview
from PyQt5.QtWebEngineWidgets import *  # Enables embedding web content using the Chromium engine
from PyQt5.QtSql import *               # Functionality for working with databases
from PyQt5.QtSvg import *               # Support for displaying and manipulating SVG images
from PyQt5.QtXml import *               # Functionality for working with XML data
from PyQt5.QtBluetooth import *         # Classes for Bluetooth functionality
from PyQt5.QtChart import *             # Module for creating applications
from PyQt5.QtQml import *               # Enables creating applications using QML and JavaScript
from PyQt5.QtLocation import *          # Classes for mapping and location services
from PyQt5.QtWebChannel import *        # Enables communications between QML/HTML and C++
from PyQt5.QtWebSockets import *        # Functionality for WebSocket communication
from PyQt5.QtSerialPort import *        # Classes for serial port communication
from PyQt5.QtSensors import *           # Access to system sensors
from PyQt5.QtTest import *              # Framework for unit testing PyQt applications
from PyQt5.QtOpenGL import *            # Classes for rendering 3D graphics using OpenGL
from PyQt5.QtRemoteObjects import *     # Enables inter-process communication using remote objects
from PyQt5.QtNfc import *               # Classes for Near Field Communication (NFC)
from PyQt5.QtQuick import *             # Framework for building user interfaces with fluid animations and effects
from PyQt5.QtQuickWidgets import *      # Widgets for using Qt Quick content in traditional widget-based applications
from PyQt5.QtXmlPatterns import *       # Support for XQuery and XPath 



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Declare objects
        self.line_edit = QLineEdit(self)
        self.initUI()

    def initUI(self):   # initialize User Interface
        self.setWindowTitle("Window Title")
        self.setGeometry(0, 2, 700, 500)       # x, y, width, height
        self.setWindowIcon(QIcon("filename.jpg"))

        self.button = QPushButton("Button", self)
        self.button.clicked.connect(self.on_click)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        grid = QGridLayout()                    # Layout manager: QGridLayout, QHBoxLayout, QVBoxLayout
        grid.addWidget(self.button, 0, 0)
        central_widget.setLayout(grid)

        
        self.setStyleSheet("""QPushButton{font-size: 40px; font-family: Arial; 
                           padding: 15px 75px; margin: 25px; 
                           border: 3px solid; border-radius: 15px; 
                           background-color: hsl(204, 100%, 64%);} 
                           QPushButton:hover{background-color: hsl(204, 100%, 84%);}""")

    def on_click(self):
        pass

    def submit(self):
        input = self.line_edit.input()



if __name__ == "__main__":
    app = QApplication(sys.argvs)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())       # exec_() no longer supported in PyQt6