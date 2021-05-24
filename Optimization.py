from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable
import pandas as pd
import numpy as np
from Data import *
import pprint

class Optimize:
    def __init__(self):
        self.data = Data.get_instance()

    def optimize(self):
        pprint.pprint(self.data.wstawione_dane)

        problem = LpProblem("Dobor optymalnego asortymentu", LpMaximize)

        naklady = [self.data.wstawione_dane["produkt"+str(i)] for i in range(self.data.produkty_no)]
        print(naklady)
        zyski = self.data.wstawione_dane["zyski_jednostkowe"]
        gorne_ograniczenie_produktu = self.data.wstawione_dane["max_produkt"]        
        dolne_ograniczenie_produktu = self.data.wstawione_dane["min_produkt"]
        gorne_ograniczenie_fabryki = self.data.wstawione_dane["max_fabryka"]
        nums = [i for i in range(self.data.produkty_no)]
        nazwy = ["P"+str(num) for num in nums]
        
        vars = [LpVariable(name, None, cat="Integer") for name in nazwy]
        problem += lpSum(float(zyski[i]) * vars[i] for i in range(0, self.data.produkty_no))

        for i in range(self.data.srodki_produkcji_no):
            problem += lpSum([float(naklady[j][i]) * vars[j] for j in range(len(vars))]) <= gorne_ograniczenie_fabryki[i]

        for i in range(self.data.produkty_no):
            problem += lpSum([vars[i]]) <= gorne_ograniczenie_produktu[i]
        
        for i in range(self.data.produkty_no):
            problem += lpSum([vars[i]]) >= dolne_ograniczenie_produktu[i]

        print(problem)
        problem.solve()
        zoptymalizowane = []
        for v in problem.variables():
            zoptymalizowane.append(v.varValue)

        for i in range(self.data.produkty_no):
            self.data.produkty_ilosc[i] = zoptymalizowane[i]
        
        self.data.wartosc_funkcji_celu = problem.objective.value()