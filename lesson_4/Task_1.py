# Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках
# домашнего задания первых трех уроков
# В диапазоне натуральных чисел от 2 до n определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.
import cProfile

# 1 вариант
def main(n):
    a = [0] * 8
    b = [i for i in range(2, n)]

    for i in b:
        if i % 2 == 0:
            a[0] += 1
        if i % 3 == 0:
            a[1] += 1
        if i % 4 == 0:
            a[2] += 1
        if i % 5 == 0:
            a[3] += 1
        if i % 6 == 0:
            a[4] += 1
        if i % 7 == 0:
            a[5] += 1
        if i % 8 == 0:
            a[6] += 1
        if i % 9 == 0:
            a[7] += 1
    return a


# E:\Dropbox\algorithm\lesson_4>python -m timeit -n 100 -s "import Task_1" "Task_1.main(100)"
# 100 loops, best of 3: 71.5 usec per loop
#
# E:\Dropbox\algorithm\lesson_4>python -m timeit -n 100 -s "import Task_1" "Task_1.main(500)"
# 100 loops, best of 3: 349 usec per loop
#
# E:\Dropbox\algorithm\lesson_4>python -m timeit -n 100 -s "import Task_1" "Task_1.main(1000)"
# 100 loops, best of 3: 699 usec per loop
#
# E:\Dropbox\algorithm\lesson_4>python -m timeit -n 100 -s "import Task_1" "Task_1.main(1000000)"
# 100 loops, best of 3: 1.12 sec per loop

# cProfile.run('main(500)')
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
   #      1    0.000    0.000    0.000    0.000 Task_1.py:7(main)
   #      1    0.000    0.000    0.000    0.000 Task_1.py:9(<listcomp>)
   #      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run('main(1000)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.001    0.001    0.001    0.001 Task_1.py:7(main)
#         1    0.000    0.000    0.000    0.000 Task_1.py:9(<listcomp>)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run('main(1000000)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.015    0.015    1.230    1.230 <string>:1(<module>)
#         1    1.149    1.149    1.216    1.216 Task_1.py:7(main)
#         1    0.067    0.067    0.067    0.067 Task_1.py:9(<listcomp>)
#         1    0.000    0.000    1.231    1.231 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# 2 вариант
def main_2(n):
    a = [0] * 8
    b = [i for i in range(2, n)]
    i = 2
    while i <= 9:
        for num in b:
            if num % i == 0:
                a[i - 2] += 1
        i += 1
    return a
# E:\Dropbox\algorithm\lesson_4>python -m timeit -n 100 -s "import Task_1" "Task_1.main_2(100)"
# 100 loops, best of 3: 93.8 usec per loop
#
# E:\Dropbox\algorithm\lesson_4>python -m timeit -n 100 -s "import Task_1" "Task_1.main_2(500)"
# 100 loops, best of 3: 475 usec per loop
#
# E:\Dropbox\algorithm\lesson_4>python -m timeit -n 100 -s "import Task_1" "Task_1.main_2(1000)"
# 100 loops, best of 3: 935 usec per loop
#
# E:\Dropbox\algorithm\lesson_4>python -m timeit -n 100 -s "import Task_1" "Task_1.main_2(1000000)"
# 100 loops, best of 3: 1.35 sec per loop

# cProfile.run('main_2(500)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.001    0.001    0.001    0.001 Task_1.py:68(main_2)
#         1    0.000    0.000    0.000    0.000 Task_1.py:70(<listcomp>)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run('main_2(1000)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#         1    0.002    0.002    0.002    0.002 Task_1.py:68(main_2)
#         1    0.000    0.000    0.000    0.000 Task_1.py:70(<listcomp>)
#         1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run('main_2(1000000)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.016    0.016    1.494    1.494 <string>:1(<module>)
#         1    1.409    1.409    1.478    1.478 Task_1.py:68(main_2)
#         1    0.069    0.069    0.069    0.069 Task_1.py:70(<listcomp>)
#         1    0.000    0.000    1.495    1.495 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}