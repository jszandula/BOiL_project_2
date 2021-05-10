from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable

model = LpProblem(name="some-problem", sense=LpMaximize)

x = LpVariable(name='x', lowBound=0)
y = LpVariable(name='y', lowBound=0)


expression = 2 * x + 4 * y            
type(expression)

constraint = 2 * x + 4 * y >= 8
type(constraint)

model += (16 * x + 24 * y <= 96000, "red_constraint")        # dodajemy ograniczenia
model += (16 * x + 10 * y <= 80000, "blue_constraint")
model += (x <= 3000, "yellow_constraint")
model += (y <= 4000, "green_constraint")
#model += (x = 2/3 * y, "black_constraint")     # to nie wiem jak zrobic xd

model += 30 * x + 40 * y            # to co maksymalizujemy

#model += lpSum([x, 2 * y])      # mozna tez tak

status = model.solve()
print(f"status: {model.status}, {LpStatus[model.status]}")
print(f"objective: {model.objective.value()}")
for var in model.variables():
    print(f"{var.name}: {var.value()}")
for name, constraint in model.constraints.items():
    print(f"{name}: {constraint.value()}")
