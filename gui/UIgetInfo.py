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

        '''COMPONENTS'''
        self.produkty = QLabel("Liczba produktow(kolummny): ")
        self.produkty_no = QLineEdit()
        self.produkty_no.setValidator(QIntValidator())

        self.srodki_produkcji_no = QLabel("Srodki produkcji(wiersze): ")
        self.srodki_produkcji_no = QLineEdit()
        self.srodki_produkcji_no.setValidator(QIntValidator())

        self.submit_btn = QPushButton("Dalej")

        '''LAYOUT'''
        self.layout.addWidget(self.produkty)
        self.layout.addWidget(self.produkty_no)
        self.layout.addWidget(self.srodki_produkcji_no)
        self.layout.addWidget(self.srodki_produkcji_no)
        self.layout.addWidget(self.submit_btn)

        self.setLayout(self.layout)

    # OBSOLETE FUNC
    def get_data(self):
        self.data.produkty_no = int(self.produkty_no.text())
        self.data.srodki_produkcji_no = int(self.srodki_produkcji_no.text())
        print(f"prod: {self.data.produkty_no}, srodki_produkcji_no: {self.data.srodki_produkcji_no}")
