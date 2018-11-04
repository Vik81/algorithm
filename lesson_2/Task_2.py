num = input('Введите число: ')
s = 0
n = 0

for i in num:
    if int(i) % 2 == 0:
        s += 1
    else:
        n += 1

print('четных - {}, нечетных - {}'.format(s, n))