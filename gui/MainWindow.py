from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from settings import *
from gui.UIgetInfo import UIgetInfo
from Data import Data


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.data = Data.get_instance()
        self.welcoming_screen()

    def welcoming_screen(self):
        self.setMinimumWidth(SCR_SIZE[0])
        self.setMinimumHeight(SCR_SIZE[1])
        self.UIgetInfo = UIgetInfo(self)
        self.setCentralWidget(self.UIgetInfo)
        self.show()

    def data_input(self):
        print("data_input")

    def results(self):
        print("result")