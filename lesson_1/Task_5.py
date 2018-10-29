b = input('Введите первую букву: ')
c = input('Введите вторую букву: ')

n = ord('a')
m = ord(b) - n + 1
k = ord(c) - n + 1

print('Место первой буквы - {}'.format(m))
print('Место второй буквы - {} буква'.format(k))

n = k - m - 1

print('Растояние между буквами = {}'. format(n))