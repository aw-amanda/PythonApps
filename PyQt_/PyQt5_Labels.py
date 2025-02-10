# PyQt5 QLabels

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont   #QFont class allows you to use fonts
from PyQt5.QtCore import Qt # Qt class is used for alignments

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)

        label = QLabel("Hell0", self)
        label.setFont(QFont("Arial", 40))
        label.setGeometry(0, 0, 500, 100)
        label.setStyleSheet("color: #9477bf;"  
                            "background-color: #7c7c7d"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;")
        # use setAlignment method with Qt class with Align flag to align label:

            # align text vertically to the top: label.setAlignment(Qt.AlignTop) 
            # align vertically on the bottom: label.setAlignment(Qt.AlignBottom)
            # align vertically in the center: label.setAlignment(Qt.AlignVCenter)

            # align horizontally right: label.setAlignment(Qt.AlignRight)
            # align horizontally in the center: label.setAlignment(Qt.AlignHCenter)
            # align horizontally left: label.setAlignment(Qt.AlignLeft)

        # Combine both horizontal and vertical positioning (use the | ('or' bitwise operator) to combine flags):
            # align to horizontal center and top: label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)  
            # align to center and bottom: label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)
            # align to horizontal center and vertical center: label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        # Shortcut for the very center:
        label.setAlignment(Qt.AlignCenter)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()