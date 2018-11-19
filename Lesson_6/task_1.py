# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых
# трех уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.

# Windows 10 64-bit,  Python 3.6.5 32-bit

import sys
size_value = [] # обнулять перед запуском 2 варианта
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

# 1 вариант
a = [0] * 8
b = [i for i in range(2, 100)]

for i in b:
    if i % 2 == 0:
        a[0] += 1
    if i % 3 == 0:
        a[1] += 1
    if i % 4 == 0:
        a[2] += 1
    if i % 5 == 0:
        a[3] += 1
    if i % 6 == 0:
        a[4] += 1
    if i % 7 == 0:
        a[5] += 1
    if i % 8 == 0:
        a[6] += 1
    if i % 9 == 0:
        a[7] += 1
print(a)
show_size(i)
print(sum(size_value))
show_size(a)
print(sum(size_value))
show_size(b)
print(sum(size_value))

# type=<class 'int'>, size=14, object=99
# 14
#  type=<class 'list'>, size=68, object=[49, 33, 24, 19, 16, 14, 12, 11]
# 	 type=<class 'int'>, size=14, object=49
# 	 type=<class 'int'>, size=14, object=33
# 	 type=<class 'int'>, size=14, object=24
# 	 type=<class 'int'>, size=14, object=19
# 	 type=<class 'int'>, size=14, object=16
# 	 type=<class 'int'>, size=14, object=14
# 	 type=<class 'int'>, size=14, object=12
# 	 type=<class 'int'>, size=14, object=11
# 194
#  type=<class 'list'>, size=460, object=[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
# 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49,
# 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77,
#  78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
# 	 type=<class 'int'>, size=14, object=2
# 	 type=<class 'int'>, size=14, object=3
# 	 type=<class 'int'>, size=14, object=4
# 	 type=<class 'int'>, size=14, object=5
# 	 type=<class 'int'>, size=14, object=6
# 	 type=<class 'int'>, size=14, object=7
# 	 type=<class 'int'>, size=14, object=8
# 	 type=<class 'int'>, size=14, object=9
# 	 type=<class 'int'>, size=14, object=10
# 	 type=<class 'int'>, size=14, object=11
# 	 type=<class 'int'>, size=14, object=12
# 	 type=<class 'int'>, size=14, object=13
# 	 type=<class 'int'>, size=14, object=14
# 	 type=<class 'int'>, size=14, object=15
# 	 type=<class 'int'>, size=14, object=16
# 	 type=<class 'int'>, size=14, object=17
# 	 type=<class 'int'>, size=14, object=18
# 	 type=<class 'int'>, size=14, object=19
# 	 type=<class 'int'>, size=14, object=20
# 	 type=<class 'int'>, size=14, object=21
# 	 type=<class 'int'>, size=14, object=22
# 	 type=<class 'int'>, size=14, object=23
# 	 type=<class 'int'>, size=14, object=24
# 	 type=<class 'int'>, size=14, object=25
# 	 type=<class 'int'>, size=14, object=26
# 	 type=<class 'int'>, size=14, object=27
# 	 type=<class 'int'>, size=14, object=28
# 	 type=<class 'int'>, size=14, object=29
# 	 type=<class 'int'>, size=14, object=30
# 	 type=<class 'int'>, size=14, object=31
# 	 type=<class 'int'>, size=14, object=32
# 	 type=<class 'int'>, size=14, object=33
# 	 type=<class 'int'>, size=14, object=34
# 	 type=<class 'int'>, size=14, object=35
# 	 type=<class 'int'>, size=14, object=36
# 	 type=<class 'int'>, size=14, object=37
# 	 type=<class 'int'>, size=14, object=38
# 	 type=<class 'int'>, size=14, object=39
# 	 type=<class 'int'>, size=14, object=40
# 	 type=<class 'int'>, size=14, object=41
# 	 type=<class 'int'>, size=14, object=42
# 	 type=<class 'int'>, size=14, object=43
# 	 type=<class 'int'>, size=14, object=44
# 	 type=<class 'int'>, size=14, object=45
# 	 type=<class 'int'>, size=14, object=46
# 	 type=<class 'int'>, size=14, object=47
# 	 type=<class 'int'>, size=14, object=48
# 	 type=<class 'int'>, size=14, object=49
# 	 type=<class 'int'>, size=14, object=50
# 	 type=<class 'int'>, size=14, object=51
# 	 type=<class 'int'>, size=14, object=52
# 	 type=<class 'int'>, size=14, object=53
# 	 type=<class 'int'>, size=14, object=54
# 	 type=<class 'int'>, size=14, object=55
# 	 type=<class 'int'>, size=14, object=56
# 	 type=<class 'int'>, size=14, object=57
# 	 type=<class 'int'>, size=14, object=58
# 	 type=<class 'int'>, size=14, object=59
# 	 type=<class 'int'>, size=14, object=60
# 	 type=<class 'int'>, size=14, object=61
# 	 type=<class 'int'>, size=14, object=62
# 	 type=<class 'int'>, size=14, object=63
# 	 type=<class 'int'>, size=14, object=64
# 	 type=<class 'int'>, size=14, object=65
# 	 type=<class 'int'>, size=14, object=66
# 	 type=<class 'int'>, size=14, object=67
# 	 type=<class 'int'>, size=14, object=68
# 	 type=<class 'int'>, size=14, object=69
# 	 type=<class 'int'>, size=14, object=70
# 	 type=<class 'int'>, size=14, object=71
# 	 type=<class 'int'>, size=14, object=72
# 	 type=<class 'int'>, size=14, object=73
# 	 type=<class 'int'>, size=14, object=74
# 	 type=<class 'int'>, size=14, object=75
# 	 type=<class 'int'>, size=14, object=76
# 	 type=<class 'int'>, size=14, object=77
# 	 type=<class 'int'>, size=14, object=78
# 	 type=<class 'int'>, size=14, object=79
# 	 type=<class 'int'>, size=14, object=80
# 	 type=<class 'int'>, size=14, object=81
# 	 type=<class 'int'>, size=14, object=82
# 	 type=<class 'int'>, size=14, object=83
# 	 type=<class 'int'>, size=14, object=84
# 	 type=<class 'int'>, size=14, object=85
# 	 type=<class 'int'>, size=14, object=86
# 	 type=<class 'int'>, size=14, object=87
# 	 type=<class 'int'>, size=14, object=88
# 	 type=<class 'int'>, size=14, object=89
# 	 type=<class 'int'>, size=14, object=90
# 	 type=<class 'int'>, size=14, object=91
# 	 type=<class 'int'>, size=14, object=92
# 	 type=<class 'int'>, size=14, object=93
# 	 type=<class 'int'>, size=14, object=94
# 	 type=<class 'int'>, size=14, object=95
# 	 type=<class 'int'>, size=14, object=96
# 	 type=<class 'int'>, size=14, object=97
# 	 type=<class 'int'>, size=14, object=98
# 	 type=<class 'int'>, size=14, object=99
#  Итого переенные занимают: 2026 b



# 2 вариант
a = [0] * 8
i = 2

while i <= 9:
    for num in b:
        if num % i == 0:
            a[i - 2] += 1
    i += 1
print(a)

size_value = []
print(a)
show_size(i)
print(sum(size_value))
show_size(a)
print(sum(size_value))

#  type=<class 'int'>, size=14, object=10
# 14
#  type=<class 'list'>, size=68, object=[49, 33, 24, 19, 16, 14, 12, 11]
# 	 type=<class 'int'>, size=14, object=49
# 	 type=<class 'int'>, size=14, object=33
# 	 type=<class 'int'>, size=14, object=24
# 	 type=<class 'int'>, size=14, object=19
# 	 type=<class 'int'>, size=14, object=16
# 	 type=<class 'int'>, size=14, object=14
# 	 type=<class 'int'>, size=14, object=12
# 	 type=<class 'int'>, size=14, object=11
# Итого переенные занимают: 194
