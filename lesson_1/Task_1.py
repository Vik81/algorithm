x = int(input('Введите трехзначное число: '))

a = x // 100
b = x % 100 // 10
c = x % 10
print('Сумма чисел {}, {}, {} = {}'.format(a, b, c, a + b + c))
print('Произведение чисел {}, {}, {} = {}'.format(a, b, c, a * b * c))