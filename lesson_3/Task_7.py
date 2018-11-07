# В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой
# (оба являться минимальными), так и различаться.
import random

SIZE = 10
a = [random.randint(0, 50) for _ in range(SIZE)]
min_1 = 0
min_2 = 0

for i in range(SIZE):
    if a[i] < a[min_1]:
        min_1 = i
for i in range(SIZE):
    if i != min_1:
        if a[i] < a[min_2]:
            min_2 = i

print(a)
print('первое минимальное число: позиция - {}, число {}'.format(min_1, a[min_1]))
print('второе минимальное число: позиция - {}, число {}'.format(min_2, a[min_2]))