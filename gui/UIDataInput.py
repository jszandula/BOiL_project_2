from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QGridLayout, QHBoxLayout, QVBoxLayout, QMessageBox, QLineEdit, \
    QFormLayout, QTableWidget
from PyQt5.QtGui import QCursor, QPixmap, QFont, QIntValidator
from PyQt5 import QtCore
from settings import *
from Data import *
import pprint


class UIDataInput(QWidget):
    def __init__(self, parent=None):
        super(UIDataInput, self).__init__(parent)
        self.data = Data.get_instance()
        self.initUI()

    def initUI(self):
        self.layout = QGridLayout()
        self.createTable()
        self.createTable2()

        buttonHBox = QHBoxLayout()
        self.zapisz_dane = QPushButton("Zapisz dane")
        self.zapisz_dane.clicked.connect(self.zapisz_dane_onclick)

        self.submit_btn = QPushButton("Dalej")

        buttonHBox.addWidget(self.zapisz_dane)
        buttonHBox.addWidget(self.submit_btn)

        self.layout.addLayout(buttonHBox, 2, 0)

        self.setLayout(self.layout)

    def createTable(self):
        vbox = QVBoxLayout()
        # produkty sa dawane na koncu bo mozna by bylo ich dodawac w nieskonczonosc
        # a kilka rzeczy zawszze musi byc w tej tabeli jak np cena
        # pomimo tego ze najlepsza cena to gratis :)
        self.columns = ['zyski_jednostkowe', 'max_produkt', 'min_produkt']

        self.table = QTableWidget()
        self.table.setRowCount(self.data.produkty_no)
        self.table.setColumnCount(len(self.columns))
        self.table.setHorizontalHeaderLabels(self.columns)
        vbox.addWidget(self.table)
        self.layout.addLayout(vbox, 0, 0)

    def createTable2(self):
        vbox = QVBoxLayout()
        self.columns2 = ['max_fabryka']
        prod_str = FAB_PROD
        for i in range(self.data.produkty_no):
            new_str = prod_str + str(i)
            self.columns2.append(new_str)

        self.table2 = QTableWidget()
        self.table2.setRowCount(self.data.tworzyciele_no)
        self.table2.setColumnCount(len(self.columns2))
        self.table2.setHorizontalHeaderLabels(self.columns2)
        vbox.addWidget(self.table2)
        self.layout.addLayout(vbox, 1, 0)

    def zapisz_dane_onclick(self):
        columns = []
        for i in self.columns:
            columns.append(i)

        for i in self.columns2:
            columns.append(i)

        for i in columns:
            self.data.inserted_data[i] = []

        for i in range(self.data.produkty_no):
            for j in range(len(self.columns)):
                self.data.inserted_data[self.columns[j]].append(int(self.table.item(i, j).text()))

        for i in range(self.data.tworzyciele_no):
            for j in range(len(self.columns2)):
                self.data.inserted_data[self.columns2[j]].append(int(self.table2.item(i, j).text()))

        pprint.pprint(self.data.inserted_data)
