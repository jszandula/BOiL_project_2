from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable
import pandas as pd
import numpy as np
from Data import *
import pprint

class Optimize:
    def __init__(self):
        self.data = Data.get_instance()

    def optimize(self):
        pprint.pprint(self.data.inserted_data)

        problem = LpProblem("Some metale shiet", LpMaximize)

        # fabrics_num = int(input("\nPodaj liczbe fabryk/fabrykatow: "))
        # products_num = int(input("\nPodaj liczbe produktow: "))

        # names = []
        # for i in range(0, products_num):
        #     names.append("P"+str(i+1))

        costs = [self.data.inserted_data["produkt"+str(i)] for i in range(self.data.produkty_no)]
        print(costs)
        gains = self.data.inserted_data["zyski_jednostkowe"]
        product_upper_constraints = self.data.inserted_data["max_produkt"]        
        product_lower_constraints = self.data.inserted_data["min_produkt"]
        fabric_upper_constraints = self.data.inserted_data["max_fabryka"]
        nums = [i for i in range(self.data.produkty_no)]
        names = ["P"+str(num) for num in nums]
        # for i in range(0, self.data.produkty_no):
        #     for j in range(0, self.data.tworzyciele_no):
        #         costs[i,j] = int(input("Podaj koszt dla {:d} produktu {:d} fabryki: ".format(i+1,j+1)))

        # for i in range(0, self.data.produkty_no):
        #     gains[i] = int(input("Podaj zysk z {:d} produktu: ".format(i+1)))
        #     product_upper_constraints[i] = int(input("Podaj gorne ograniczenie dla {:d} produktu: ".format(i+1)))

        # for i in range(0, self.data.tworzyciele_no):
        #     fabric_upper_constraints[i] = int(input("Podaj gorne ograniczenie dla {:d} fabryki/fabrykatu: ".format(i+1)))

        vars = [LpVariable(name, lowBound=0, cat="Integer") for name in names]
        problem += lpSum(int(gains[i]) * vars[i] for i in range(0, self.data.produkty_no))

        for i in range(self.data.tworzyciele_no):
            problem += lpSum([int(costs[j][i]) * vars[j] for j in range(len(vars))]) <= fabric_upper_constraints[i]

        for i in range(self.data.produkty_no):
            problem += lpSum([vars[i]]) <= product_upper_constraints[i]

        print(problem)
        problem.solve()
        optimized = []
        for v in problem.variables():
            optimized.append(v.varValue)

        for i in range(self.data.produkty_no):
            self.data.produkty_ilosc[i] = optimized[i]
        
        self.data.wartosc_funkcji_celu = problem.objective.value()