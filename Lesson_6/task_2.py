# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых
# трех уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

# Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со
# # значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 –
# # если индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.

# Windows 10 64-bit,  Python 3.6.5 32-bit
import sys

size_value = []
def show_size(x, level=0):
    print('\t' * level, f'type={type(x)}, size={sys.getsizeof(x)}, object={x}')
    size_value.append(sys.getsizeof(x))
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                show_size(key, level + 1)
                show_size(value, level + 1)
        elif not isinstance(x, str):
            for item in x:
                show_size(item, level + 1)


import random

SIZE = 10
a = [random.randint(0, 50) for _ in range(SIZE)]
even = []
for i in a:
    if i % 2 == 0:
        even.append(a.index(i))

print(a)
print(even)

show_size(SIZE)
print(sum(size_value))
show_size(a)
print(sum(size_value))
show_size(i)
print(sum(size_value))

# type=<class 'int'>, size=14, object=10
# 14
#  type=<class 'list'>, size=100, object=[28, 17, 3, 32, 32, 34, 44, 25, 47, 22]
# 	 type=<class 'int'>, size=14, object=28
# 	 type=<class 'int'>, size=14, object=17
# 	 type=<class 'int'>, size=14, object=3
# 	 type=<class 'int'>, size=14, object=32
# 	 type=<class 'int'>, size=14, object=32
# 	 type=<class 'int'>, size=14, object=34
# 	 type=<class 'int'>, size=14, object=44
# 	 type=<class 'int'>, size=14, object=25
# 	 type=<class 'int'>, size=14, object=47
# 	 type=<class 'int'>, size=14, object=22
# 254
#  type=<class 'int'>, size=14, object=22
# Итого переенные занимают: 268 b