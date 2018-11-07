# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
import random

SIZE = 10
a = [random.randint(-50, 50) for _ in range(SIZE)]
ind = -1
print(a)

for i in range(SIZE):
    if a[i] < 0 and ind == -1:
        ind = i
    elif a[i] < 0 and a[i] > a[ind]:
        ind = i

print('позиция в массиве - {}, значение элемента - {}'.format(ind, a[ind]))
