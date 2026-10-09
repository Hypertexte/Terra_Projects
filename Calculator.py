import random as random
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button_is_checked = True 
        self.setWindowTitle("!")
        button = QPushButton('Boutton')
        button.setFixedSize(QSize(200,150))
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_toggled)
        button.setChecked(self.button_is_checked)
        self.setMinimumSize(QSize(200,150))
        self.setCentralWidget(button)

    
    def the_button_was_toggled(self, checked):
        self.button_is_checked = checked
        print(self.button_is_checked)

app = QApplication(sys.argv)
window = MainWindow()
window.show()  #By default hidden   DONT DELETE CANT STOP THE APP IF NOT HERE 

app.exec() #Start the loop of event

