year = int(input('Введите год: '))

if year % 4 == 0:
    if year % 100 != 0:
        print('Год високосный')
    elif year % 400 == 0:
        print('Год високосный')
    else:
        print('Год обычный')
else:
    print('Год обычный')