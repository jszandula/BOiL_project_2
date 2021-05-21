from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QGridLayout, QHBoxLayout, QVBoxLayout, QMessageBox, QLineEdit, QFormLayout, QTableWidget
from PyQt5.QtGui import QCursor, QPixmap, QFont, QIntValidator
from PyQt5 import QtCore
from settings import *
from Data import *

class UIResult(QWidget):
    def __init__(self, parent=None):
        super(UIResult, self).__init__(parent)
        self.data = Data.get_instance()
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.f_v_bl = QLabel(f"Wartość funkcji celu: {self.data.wartosc_funkcji_celu}")

        self.layout.addWidget(self.f_v_bl)
        self.setLayout(self.layout)