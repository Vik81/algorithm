# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
import random

SIZE = 10
a = [random.randint(0, 50) for _ in range(SIZE)]
a_min = 0
a_max = 0
summ = 0

for i in range(len(a)):
    if a[i] < a[a_min]:
        a_min = i
    if a[i] > a[a_max]:
        a_max = i

if a_max < a_min:
    a_max, a_min = a_min, a_max
print(a_min, a_max)
for i in range(a_min + 1, a_max):
    summ += a[i]
print(a)
print('Сумма чисел между минимальным и максиальным элементами = {}'.format(summ))
