from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from importWordsFromFile import *

app = QApplication([])

app.setStyle('Fusion')

window = QWidget()

layout = QVBoxLayout()
buttonTop = QPushButton('Top')
buttonBot = QPushButton()
layout.addWidget(buttonTop)
layout.addWidget(buttonBot)
window.setLayout(layout)

def on_button_clicked():
    alert = QMessageBox()
    alert.setText("Clicked")
    alert.exec()

buttonTop.clicked.connect(on_button_clicked)
buttonBot.clicked.connect(on_button_clicked)

buttonTop.setStyleSheet("""
                        QPushButton { background-color: rgb(247,225,176);
                        border-color: rgb(246,227,178);
                        border-width: 5px;
                        border-style: outset;
                        font: bold 14px;
                        padding: 15px;
                        min-width: 10em;
                        margin: 5px;
                        }   
                        QPushButton:pressed{
                        background-color: rgb(222,200,151);
                        border-style: inset;
                        }                  
                        """)

window.show()
app.exec()