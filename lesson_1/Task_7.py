a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print('Равносторонний')
    elif a == b or a == c or b == c:
        print('Равнобедренный')
    else:
        print('Разносторонний')
else:
    print('Треугольник не существует')