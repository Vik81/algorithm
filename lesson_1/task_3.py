print('Введите координаты двух точек')
x1 = float(input('введите координату x первой точки: '))
y1 = float(input('введите координату y первой точки: '))
x2 = float(input('введите координату x второй точки: '))
y2 = float(input('введите координату y второй точки: '))

k = (y2 - y1) / (x2 - x1)

print('y = {} * (x - {}) + {}'.format(k, x1, y1))
# y = k * (x - x1) + y1
