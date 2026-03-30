#imports
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

#main class
class Window(QMainWindow):

    #Constructor method
    def __init__(self):
        #Inherits method from superclass (QMainWindow)
        super().__init__()

        self.UiComponents()

    def UiComponents(self):
        #Window Name
        self.setWindowTitle("Ascii Art")
        self.setWindowIcon(QtGui.QIcon("Ascii-Icon.png"))
        
        #Title
        head = QLabel("Turn Something into Ascii!", self)
        head.width, head.height = 400, 60
        head.setGeometry(0, 10, head.width, head.height)
        font = QFont("Jokerman", 15)
        font.setBold(True)
        head.setFont(font)
        head.setAlignment(Qt.AlignCenter)
        color = QGraphicsColorizeEffect(self)
        color.setColor(Qt.white)
        head.setGraphicsEffect(color)

        #properties of window
        self.setObjectName("MainWidget")
        self.setStyleSheet("""
            #MainWidget{
                           background-color: black;
                        }
        """)

        #Input field goes here
        self.tbx = QLineEdit(self)
        #properties
        self.tbx.width, self.tbx.height = 200, 20
        self.tbx.setGeometry(100, 70, self.tbx.width, self.tbx.height)
        self.tbx.setAlignment(Qt.AlignCenter)
        self.tbx.setStyleSheet("""
            QLineEdit {
                    background: rgba(0, 0, 0, 0);
                    border: none;
                    color: white;
                    }
        """)
        # self.tbx.setFont(QFont(,))
        
    #------------------------------------------Show Art-----------------------------------------
        
        #art button creation
        s_art = QPushButton("Show Art", self)
        #button geometry
        s_art.width, s_art.height = 100, 20
        s_art.setGeometry(150, 100, s_art.width, s_art.height)


        #Output of Ascii Art


        #Window Geometry
        self.width = 400
        self.height = 500
        self.setGeometry(100, 100, self.width, self.height)

        self.show()



if __name__ == '__main__':

#Creates app object, initialize Qt app
    App = QApplication(sys.argv)

#Creates window class
    window = Window()

#Starts app, everything is blocked until app is exited
    sys.exit(App.exec())



