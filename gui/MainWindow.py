from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from settings import *
from gui.UIgetInfo import UIgetInfo
from gui.UIDataInput import UIDataInput
from gui.UIResult import UIResult
from Data import Data
from Optimization import Optimize


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.data = Data.get_instance()
        self.welcoming_screen()

    def welcoming_screen(self):
        self.setMinimumWidth(SCR_SIZE[0])
        self.setMinimumHeight(SCR_SIZE[1])
        self.UIgetInfo = UIgetInfo(self)
        self.UIgetInfo.submit_btn.clicked.connect(lambda: self.data_input())
        self.setCentralWidget(self.UIgetInfo)
        self.show()

    def data_input(self):
        self.data.produkty_no = int(self.UIgetInfo.produkty_no.text())
        self.data.tworzyciele_no = int(self.UIgetInfo.tworzyciele_no.text())
        self.setMinimumWidth(SCR_SIZE[0])
        self.setMinimumHeight(SCR_SIZE[1])
        self.UIDataInput = UIDataInput(self)
        self.UIDataInput.submit_btn.clicked.connect(lambda: self.results())
        self.setCentralWidget(self.UIDataInput)
        self.show()

    def results(self):
        self.optimize = Optimize()
        self.optimize.optimize()
        self.setMinimumWidth(SCR_SIZE[0])
        self.setMinimumHeight(SCR_SIZE[1])
        self.UIResult = UIResult(self)
        self.setCentralWidget(self.UIResult)
        self.show()
