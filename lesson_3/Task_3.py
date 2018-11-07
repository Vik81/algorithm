# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

SIZE = 10
a = [random.randint(0, 50) for _ in range(SIZE)]
a_min = 0
a_max = 0

for i in range(SIZE):
    if a[i] < a[a_min]:
        a_min = i
    if a[i] > a[a_max]:
        a_max = i

print(a)

spam = a[a_min]
a[a_min] = a[a_max]
a[a_max] = spam

print(a)
print('Индекс минимального элемента - {}'.format(a_min))
print('Индекс максимального элемента - {}'.format(a_max))