from pulp import LpProblem, LpMaximize, LpVariable, LpMinimize, LpSolverDefault


# Пошук максимуму
def search_max():
    # Створюємо задачу максимізації
    prob_max = LpProblem("Maximize_F", LpMaximize)

    # Визначаємо змінні
    x1 = LpVariable("x1", lowBound=0, cat='Integer')
    x2 = LpVariable("x2", lowBound=0, cat='Integer')

    # Визначаємо цільову функцію
    prob_max += 3*x1 + 4*x2, "Objective Function"

    # Визначаємо обмеження
    prob_max += 8*x1 - 5*x2 <= 40
    prob_max += 2*x1 + 5*x2 >= 10
    prob_max += -6*x1 + 5*x2 <= 60
    prob_max += 2*x1 + x2 <= 14

    LpSolverDefault.msg = 0

    prob_max.solve()

    print("Результат:")
    print("x1 =", int(x1.varValue))
    print("x2 =", int(x2.varValue))
    print("Максимальне значення фукнції:", int(prob_max.objective.value()))


# Пошук мінімуму
def search_min():
    # Визначаємо задачу мінімізації
    prob_min = LpProblem("Minimize_F", LpMinimize)

    # Визначаємо змінні
    x1 = LpVariable("x1", lowBound=0, cat='Integer')
    x2 = LpVariable("x2", lowBound=0, cat='Integer')

    # Визначаємо цільову функцію
    prob_min += 3*x1 + 4*x2, "Objective Function"

    # Визначаємо обмеження
    prob_min += 8*x1 - 5*x2 <= 40
    prob_min += 2*x1 + 5*x2 >= 10
    prob_min += -6*x1 + 5*x2 <= 60
    prob_min += 2*x1 + x2 <= 14

    LpSolverDefault.msg = 0

    prob_min.solve()
    print("Результат:")
    print("x1 =", int(x1.varValue))
    print("x2 =", int(x2.varValue))
    print("Мінімальне значення фукнції:", int(prob_min.objective.value()))


if __name__ == "__main__":
    print("Програму розробив Вальчевський П., студент групи ОІ-11сп для ЛР № 5 з Досліджень операцій, 91 варіант")
    search_max()
    print("=" * 50)
    search_min()