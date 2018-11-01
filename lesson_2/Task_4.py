num = int(input('Введите число: '))
sum = 0
run = 1
i = 1
while i <= num:
    sum += run
    run /= -2
    i += 1
print(sum)