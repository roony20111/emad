from  PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QLabel
import sys
from PyQt5.QtGui import QPixmap, QIcon
import os
from PyQt5.QtCore import QSize

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        pixmap = QPixmap(os.getcwd() + "/business.jpg")
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)
        self.resize(700, 500)
        self.move(300, 300)
        self.setWindowTitle(' ')

        Button1 = QPushButton(self)
        Button1.setIcon(QIcon("bRUnY.png"))
        Button1.setIconSize(QSize(70, 70))
        Button1.setStyleSheet('QPushButton{border: 0px solid;}')
        Button1.move(600, 10)
        Button1.clicked.connect(self.onClick)
########################################################################
        Button2 = QPushButton(self)
        Button2.setIcon(QIcon("info.png"))
        Button2.setIconSize(QSize(60, 60))
        Button2.setStyleSheet('QPushButton{border: 0px solid;}')
        Button2.move(520, 10)
        Button2.clicked.connect(self.onClick1)
######################################################################
        Button3 = QPushButton(self)
        Button3.setIcon(QIcon("settings.png"))
        Button3.setIconSize(QSize(50, 50))
        Button3.setStyleSheet('QPushButton{border: 0px solid;}')
        Button3.move(440, 10)
        Button3.clicked.connect(self.onClick2)
########################################################################
        Button4 = QPushButton(self)
        Button4.setIcon(QIcon("icon.png"))
        Button4.setIconSize(QSize(70, 70))
        Button4.setStyleSheet('QPushButton{border: 0px solid;}')
        Button4.move(360, 15)
        Button4.clicked.connect(exit)



    def onClick(self):
        self.SW = SecondWindow()
        self.SW.show()
    def onClick1(self):
        self.SW = ThairdWindow()
        self.SW.show()
    def onClick2(self):
        self.SW = forWindow()
        self.SW.show()
    def onClick3(self):
        self.fW = fiveWindow()
        self.fW.show()

class SecondWindow(QMainWindow):
    def __init__(self):
        super(SecondWindow, self).__init__()
        Button = QPushButton(self)
        #Button.clicked.connect(self.onClick3)



class ThairdWindow(QMainWindow):
    def __init__(self):
        super(ThairdWindow, self).__init__()
        lbl = QLabel('ThairdWindow', self)

class forWindow(QMainWindow):
    def __init__(self):
        super(forWindow, self).__init__()
        lbl = QLabel('forWindow', self)

class fiveWindow(QMainWindow):
    def __init__(self):
        super(fiveWindow, self).__init__()
        lbl = QLabel('fiveWindow', self)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    MW = MainWindow()
    MW.show()
    sys.exit(app.exec_())









