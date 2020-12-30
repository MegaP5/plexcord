from PyQt5 import uic, QtCore, QtGui
from PyQt5.Qt import Qt, QIcon, QSystemTrayIcon, QMenu, QAction, QUrl
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout, QMainWindow

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        uic.loadUi("app.ui", self)
        self.setFixedSize(self.size())
        self.logo.setPixmap(QtGui.QPixmap("./content/plexcord.png"))

        self.show()


app = QApplication(sys.argv)

window = MainWindow()

app.exec_()