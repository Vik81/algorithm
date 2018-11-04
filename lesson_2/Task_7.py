n = int(input('Введите число: '))
s = 0
i = 1
while i <= n:
    s += i
    i += 1
m = n * (n + 1) // 2
print(s)
print(m)