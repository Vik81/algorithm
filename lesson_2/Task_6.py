import random

n = random.randint(0, 100)
i = 1
print(n)
while i <= 10:
    x = int(input('Введите число от 0 до 100: '))
    if x < n:
        print('больше')
    elif x > n:
        print('меньше')
    else:
        print('Вы угадали с {}-й попытки'.format(i))
        break
    i += 1
else:
    print('Вы исчерпали 10 попыток. Было загадано', n)