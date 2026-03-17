#imports
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

#main class
class Window(QMainWindow):

    #Constructor method
    def __init__(self):
        #Inherits method from superclass (QMainWindow)
        super().__init__()
        #Title

        self.UiComponents()

    def UiComponents(self):
        self.setWindowTitle("Ascii Art")
        self.setWindowIcon(QtGui.QIcon("Ascii-Icon.png"))

        #Window Geometry
        self.width = 400
        self.height = 500
        self.setGeometry(100, 100, self.width, self.height)

        #properties of window
        self.setObjectName("MainWidget")
        self.setStyleSheet("""
            #MainWidget{
                           background-color: black;
                        }
        """)

        self.show()



if __name__ == '__main__':
#Creates app object, initialize Qt app
    App = QApplication(sys.argv)

#Creates window class
    window = Window()

#Starts app, everything is blocked until app is exited
    sys.exit(App.exec())
