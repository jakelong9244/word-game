import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget

def startApp():
    class MainWindow(QMainWindow):
        def __init__(self):
            super().__init__()

            self.setWindowTitle("Word Game Title")
            
            MainWidget = QWidget()
            layout = QGridLayout()
            MainWidget.setLayout(layout)
            button1 = QPushButton("Button 1")
            button2 = QPushButton("Button 2")
            button3 = QPushButton("Button 3")
            button4 = QPushButton("Button 4")
            layout.addWidget(button1,0,0)
            layout.addWidget(button2,0,1)
            layout.addWidget(button3,1,0)
            layout.addWidget(button4,1,1)

            MainWidget.setStyleSheet("""
                        QPushButton { background-color: rgb(247,225,176);
                        border-color: rgb(246,227,178);
                        border-width: 5px;
                        border-style: outset;
                        font: bold 14px;
                        padding: 15px;
                        min-width: 10em;
                        margin: 0px;
                        }                
                        """)

            # Set the central widget of the Window.
            self.setCentralWidget(MainWidget)
    
    app = QApplication([])

    window = MainWindow()
    window.show()
    app.exec()

startApp()