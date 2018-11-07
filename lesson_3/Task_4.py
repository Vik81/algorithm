# Определить, какое число в массиве встречается чаще всего.
import random

SIZE = 10
a = [random.randint(0, 50) for _ in range(SIZE)]

num = a[0]
max_cnt = 1
for i in range(SIZE - 1):
    cnt = 1
    for k in range(i + 1, SIZE):
        if a[i] == a[k]:
            cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt
            num = a[i]
print(a)
if max_cnt > 1:
    print('{} раз(а) встречается число {}'.format(max_cnt, cnt))
else:
    print('Все элементы уникальны')