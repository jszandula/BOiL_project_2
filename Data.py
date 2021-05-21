from settings import *


class Data:
    _instance = None

    @staticmethod
    def get_instance():
        if Data._instance == None:
            Data()
        return Data._instance

    def __init__(self):
        if Data._instance != None:
            raise Exception("To je singleton tego nie wywolasz 2 razy :)")
        else:
            Data._instance = self

        self.tworzyciele_no = -1
        self.produkty_no = -1
        self.inserted_data = {}     # data from table
        self.wartosc_funkcji_celu = 0
        self.produkty_ilosc = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # ilosc produktow jaka zostala obliczna
