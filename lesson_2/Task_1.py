print('Пргармма завершается если вместо знака оперции введен 0')


while True:
    a = float(input('Введите первое число: '))
    b = float(input('Введите второе число: '))
    z = input('Введите знак операции: ')

    if z == '0':
        break
    elif z == '+' or z == '-' or z == '*' or z == '/':
        if z == '+':
            print('Сумма чисел {} и {} = {}'.format(a, b, a + b))
        elif z == '-':
            print('Разнсть чисел {} и {} = {}'.format(a, b, a - b))
        elif z == '*':
            print('Произведение чисел {} и {} = {}'.format(a, b, a * b))
        else:
            if b != 0:
                print('Частное чисел {} и {} = {}'.format(a, b, a / b))
            else:
                print('Ошибка деления на ноль')
    else:
        print('Введен неверный знак операции')