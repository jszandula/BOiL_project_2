from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QGridLayout, QHBoxLayout, QVBoxLayout, QMessageBox, QLineEdit, QFormLayout
from PyQt5.QtGui import QCursor, QPixmap, QFont, QIntValidator
from PyQt5 import QtCore
from settings import *
from Data import *

class UIgetInfo(QWidget):
    def __init__(self, parent=None):
        super(UIgetInfo, self).__init__(parent)
        self.data = Data.get_instance()
        self.initUI()

    def initUI(self):
        self.layout = QFormLayout()

        self.produkty = QLabel("Liczba produktow: ")
        self.produkty_no = QLineEdit()
        self.produkty_no.setValidator(QIntValidator())

        self.tworzyciele = QLabel("Liczba prducentow: ")
        self.tworzyciele_no = QLineEdit()
        self.tworzyciele_no.setValidator(QIntValidator())

        self.submit_btn = QPushButton("Dalej")
        self.submit_btn.clicked.connect(self.get_data)

        self.layout.addWidget(self.produkty)
        self.layout.addWidget(self.produkty_no)

        self.layout.addWidget(self.tworzyciele)
        self.layout.addWidget(self.tworzyciele_no)
        self.layout.addWidget(self.submit_btn)

        self.setLayout(self.layout)

    def get_data(self):
        self.data.produkty_no = self.produkty_no.text()
        self.data.tworzyciele_no = self.tworzyciele_no.text()
        print(f"prod: {self.data.produkty_no}, tworzyciele: {self.data.tworzyciele_no}")
