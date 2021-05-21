from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable
import pandas as pd

problem = LpProblem("Some metale shiet", LpMaximize)

producers_num = int(input("\nEnter number of the producers: "))
products_num = int(input("\nEnter number of the products: "))

# gain = [0] * products_num
# constraints = [0] * producers_num

# for i in range(0, products_num):
#     gain[i] = int(input("\nEnter the gain for {:d} product: ".format(i+1)))

# for i in range(0, producers_num):
#     for j in range(0, products_num):
#         constraints[i] = int(input("\nEnter the constraint for {:d} producer {:d} product".format(i+1, j+1)))

df = pd.read_excel("test.xlsx", nrows=products_num)
items = list(df['Produkt'])
pret = dict(zip(items,df['Pret']))
tasma = dict(zip(items,df['Tasma']))
gain = dict(zip(items,df['Cena']))
products_constraint = list(df['Max_produkt'])
producers_constraint = list(df['Max_fabryka'])

vars = LpVariable.dicts("Produkt", items, lowBound=0, cat='Continuous')

problem += lpSum([gain[i]*vars[i] for i in items])
problem += lpSum([pret[f] * vars[f] for f in items]) <= producers_constraint[0]
problem += lpSum([tasma[f] * vars[f] for f in items]) <= producers_constraint[1]
problem += vars[items[0]] <= products_constraint[0]
problem += vars[items[1]] <= products_constraint[1]


print(problem)
problem.solve()
for v in problem.variables():
    if v.varValue>0:
        print(v.name, "=", v.varValue)

print("Total profit: ", problem.objective.value())