from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QGridLayout, QHBoxLayout, QVBoxLayout, QMessageBox, QLineEdit, QFormLayout, QTableWidget
from PyQt5.QtGui import QCursor, QPixmap, QFont, QIntValidator
from PyQt5 import QtCore
from settings import *
from Data import *

class UIDataInput(QWidget):
    def __init__(self, parent=None):
        super(UIDataInput, self).__init__(parent)
        self.data = Data.get_instance()
        self.initUI()

    def initUI(self):
        self.layout = QGridLayout()
        self.createTable()
        submit_button = QPushButton("Dalej")


        self.setLayout(self.layout)

    def createTable(self):
        vbox = QVBoxLayout()
        # produkty sa dawane na koncu bo mozna by bylo ich dodawac w nieskonczonosc a kilka rzeczy zawszze musi byc w tej tabeli jak np cena
        # pomimo tego ze najlepsza cena to gratis :)
        columns = ['Produkt', 'cena', 'max_produkt', 'max_fabryka', 'prod1', 'prod2']       
        table = QTableWidget()
        print(f"prod: {self.data.produkty_no}, tworzyciele: {self.data.tworzyciele_no}")
        table.setRowCount(self.data.tworzyciele_no)
        table.setColumnCount(self.data.produkty_no)
        table.setHorizontalHeaderLabels(columns)
        vbox.addWidget(table)
        self.layout.addLayout(vbox,0,0)