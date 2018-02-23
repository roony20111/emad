import os
import sys
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel

app = QApplication(sys.argv)

w = QWidget()
pixmap = QPixmap(os.getcwd() + "/business.jpg")
lbl = QLabel(w)
lbl.setPixmap(pixmap)
w.resize(700, 500)
w.move(300, 300)
w.setWindowTitle(' ')

Button1 = QPushButton(w)
Button1.setIcon(QIcon("bRUnY.png"))
Button1.setIconSize(QSize(70,70))
Button1.setStyleSheet('QPushButton{border: 0px solid;}')
Button1.move(600, 10)

#######################################
Button2 = QPushButton(w)
Button2.setIcon(QIcon("info.png"))
Button2.setIconSize(QSize(60,60))
Button2.setStyleSheet('QPushButton{border: 0px solid;}')
Button2.move(520, 10)
######################################
Button3 = QPushButton(w)
Button3.setIcon(QIcon("settings.png"))
Button3.setIconSize(QSize(50,50))
Button3.setStyleSheet('QPushButton{border: 0px solid;}')
Button3.move(440, 10)
####################الخروج#################

Button4 = QPushButton(w)
Button4.setIcon(QIcon("icon.png"))
Button4.setIconSize(QSize(70,70))
Button4.setStyleSheet('QPushButton{border: 0px solid;}')
Button4.move(360, 15)
Button4.clicked.connect(exit)

w.show()

sys.exit(app.exec_())