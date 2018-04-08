import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QFont
from fromTodaytoTheTest import myTodaytoTheTest
if __name__ == "__main__":      
    app = QApplication(sys.argv)   
    w = QtWidgets.QWidget()
    w.setGeometry(800,500,200,30)
    w.setWindowOpacity(0.2)
#   w.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
    w.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
    a = QtWidgets.QLabel(w)
    a.setFont(QFont("Roman times", 20, QFont.Bold))
    a.setText(' '+ myTodaytoTheTest()+ ' days left')
    w.show() 
    QTimer.singleShot(5*1000, app.quit)
    app.exec_()
