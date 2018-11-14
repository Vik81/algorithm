 # Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется
 # как массив, элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F.
 # Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
 # Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque
print('Шестнадцатеричные цыфры вводятся в нижнем регистре')
a = deque(input('Введите первое шестнадцатеричное число: '))
b = deque(input('Введите второе шестнадцатеричное число: '))

def sum_hex(a, b):
    hex_ = deque('0123456789abcdef')
    summ = deque()
    if len(a) < len(b):
        n = len(b)
        for i in range(len(a), n):
            a.extendleft('0')
    else:
        n = len(a)
        for i in range(len(b), n):
            b.extendleft('0')
    a.reverse()
    b.reverse()
    spam = 0
    for i in range(n):
        elem = hex_.index(a[i]) + hex_.index(b[i]) + spam
        if elem <= 15:
            summ.extendleft(hex_[elem])
            spam = 0
        else:
            summ.extendleft(hex_[elem % 16])
            spam = elem // 16
    if spam > 0:
        summ.extendleft(hex_[spam])
    a.reverse()
    b.reverse()
    return summ

print(sum_hex(a, b))

# умножение
hex_ = deque('0123456789abcdef')
mult = deque()
spam_mult = deque()
spam = 0

if len(a) < len(b):
    n = len(b)
    for i in range(len(a), n):
        a.extendleft('0')
else:
    n = len(a)
    for i in range(len(b), n):
        b.extendleft('0')
a.reverse()
b.reverse()
for i in range(n):
    for j in range(n):
        elem = hex_.index(a[j]) * hex_.index(b[i]) + spam
        if elem <= 15:
            spam_mult.extendleft(hex_[elem])
            spam = 0
        else:
            spam_mult.extendleft(hex_[elem % 16])
            spam = elem // 16
    if spam > 0:
        spam_mult.extendleft(hex_[spam])

    mult = sum_hex(mult, spam_mult)
    spam_mult.clear()
    spam_mult.extendleft(['0'] * (i + 1))
    spam = 0

print(mult)
