# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# (т.е. 4 отдельных числа) для каждого предприятия. Программа должна определить среднюю прибыль
# (за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего и
# отдельно вывести наименования предприятий, чья прибыль ниже среднего.

enterprises = {}
n = int(input("Количество предприятий: "))
s = 0
for i in range(n):
    ename = input(str(i + 1) + "-е предприятие: ")
    profit = 0
    for i in range(4):

        profit += int(input("Прибыль за {}-й квартал: ".format(i + 1)))
    enterprises[ename] = profit
    s += profit

avrg = s / n
print(enterprises)
print("\nСредния прибыль за год: {}. Предприятия, чья прибыль выше средне:".format(avrg))

for i in enterprises:
    if enterprises[i] > avrg:
        print(i)

print("\nСредния прибыль за год: {}. Предприятия, чья прибыль ниже средне:".format(avrg))

for i in enterprises:
    if enterprises[i] < avrg:
        print(i)