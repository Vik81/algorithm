# Написать два алгоритма нахождения i-го по счёту простого числа
import math


# Используя алгоритм «Решето Эратосфена»
# def erat(n):
siev = [i for i in range(math.nan)]

siev[1] = 0

for i in range(2, int(math.nan)):
    if siev[i] != 0:
        j = i + i
        while j < n:
            siev[j] = 0
            j += i

print(siev)
res = [i for i in siev if i != 0]
print(res)
print(len(res))
