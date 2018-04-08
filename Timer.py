import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QColorDialog, QLineEdit
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QFont
from fromTodaytoTheTest import myTodaytoTheTest

def changebackground():
    color = QColorDialog.getColor()
    if(color.isValid()):
        w.setStyleSheet('QWidget{background-color:%s}' % color.name())
#    else:
#        print('quit')
def changefontcolor():
    color = QColorDialog.getColor()
    if(color.isValid()):
        a.setStyleSheet('color:%s' % color.name())
#    else:
#        pass
        
if __name__ == "__main__":
    app = QApplication(sys.argv)   
    w = QtWidgets.QWidget()
    w.setGeometry(700,500,460,80)
    w.setWindowOpacity(0.5)
#   w.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
    w.setWindowFlags(QtCore.Qt.CustomizeWindowHint|QtCore.Qt.NoDropShadowWindowHint)

    a = QtWidgets.QLabel(w)
    a.setFont(QFont("Roman times", 50, QFont.Bold))
    a.setText(' '+ myTodaytoTheTest()+ ' days left')    

    colorbutton = QPushButton('b', w)
    colorbutton.setGeometry(440, 0, 20, 80)
    colorbutton.show()

    fontbutton = QPushButton('f', w)
    fontbutton.setGeometry(420, 0, 20, 80)
    fontbutton.show()
    
    w.show()
    colorbutton.clicked.connect(changebackground)

    fontbutton.clicked.connect(changefontcolor)
    

#    QTimer.singleShot(5*1000, app.quit)
    app.exec_()
