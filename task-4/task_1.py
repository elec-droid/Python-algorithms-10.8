"""
1. Проанализировать скорость и сложность одного любого алгоритма из
разработанных в рамках домашнего задания первых трех уроков.
Примечание. Идеальным решением будет:
    a. выбрать хорошую задачу, которую имеет смысл оценивать;
    b. написать 3 варианта кода (один у вас уже есть);
    c. проанализировать 3 варианта и выбрать оптимальный;
    d. результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили
       замеры);
    e. написать общий вывод: какой из трёх вариантов лучше и почему.
"""
# Оценивается алгоритм из задачи № 3 к уроку № 3: В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.
from random import randrange
import cProfile


def search_max_min_1(*a: list):
    a = [randrange(1, 1000) for _ in range(1000)]
    max_i = [a[0], 0]
    min_i = [a[0], 0]
    for i in range(0, len(a)):
        if max_i[0] < a[i]:
            max_i[0], max_i[1] = a[i], i
        if min_i[0] > a[i]:
            min_i[0], min_i[1] = a[i], i

    return max_i[0], min_i[0]


def search_max_min_2(*a: list):
    a = [randrange(1, 1000) for _ in range(1000)]
    _ = a[:]
    _.sort()
    return _[-1], _[0]


def search_max_min_3(*a: list):
    a = [randrange(1, 1000) for _ in range(1000)]
    return max(a), min(a)


# s = [randrange(1, 1000) for _ in range(1000)]

# cProfile.run("search_max_min_1(s)")
# cProfile.run("search_max_min_2(s)")
# cProfile.run("search_max_min_3(s)")


"""
Все приведённые алгоритмы имеют линейную сложность O(n). Самым оптимальным является вариант №3 из-за того что
используемые внутри функции max() и min() написаны на языке C и выполняются быстрее.

-- Сводная таблица времени выполнения алгоритмов. Во всех случаях выполнялось 3 цикла по 100 итераций 
размер списка   алгоритм №1    алгоритм №2     алгоритм №3
1000            506 usec        510 usec        455 usec
10000           5.25 msec       5.43 msec       4.72 msec
100000          53.6 msec       56.7 msec       48.1 msec
1000000         533 msec        598 msec        477 msec

-- ----------------------------- 1000 значений ---------------------------- --
$ python -m timeit -n 100 -r 3 -s "import task_1" "task_1.search_max_min_1()"
100 loops, best of 3: 506 usec per loop
$ python -m timeit -n 100 -r 3 -s "import task_1" "task_1.search_max_min_2()"
100 loops, best of 3: 510 usec per loop
$ python -m timeit -n 100 -r 3 -s "import task_1" "task_1.search_max_min_3()"
100 loops, best of 3: 455 usec per loop

-- ---------------------------- 10 000 значений --------------------------- --
$ python -m timeit -n 100 -r 3 -s "import task_1" "task_1.search_max_min_1()"
100 loops, best of 3: 5.25 msec per loop
$ python -m timeit -n 100 -r 3 -s "import task_1" "task_1.search_max_min_2()"
100 loops, best of 3: 5.43 msec per loop
$ python -m timeit -n 100 -r 3 -s "import task_1" "task_1.search_max_min_3()"
100 loops, best of 3: 4.72 msec per loop

-- --------------------------- 100 000 значений --------------------------- --
$ python -m timeit -n 100 -r 3 -s "import task_1" "task_1.search_max_min_1()"
100 loops, best of 3: 53.6 msec per loop
$ python -m timeit -n 100 -r 3 -s "import task_1" "task_1.search_max_min_2()"
100 loops, best of 3: 56.7 msec per loop
$ python -m timeit -n 100 -r 3 -s "import task_1" "task_1.search_max_min_3()"
100 loops, best of 3: 48.1 msec per loop

-- -------------------------- 1 000 000 значений -------------------------- --
$ python -m timeit -n 100 -r 3 -s "import task_1" "task_1.search_max_min_1()"
100 loops, best of 3: 533 msec per loop
$ python -m timeit -n 100 -r 3 -s "import task_1" "task_1.search_max_min_2()"
100 loops, best of 3: 598 msec per loop
$ python -m timeit -n 100 -r 3 -s "import task_1" "task_1.search_max_min_3()"
100 loops, best of 3: 477 msec per loop


-- Результат cProfile.run для списка из 1000000 со случайными значениями от 1 до 1000000
cProfile.run("search_max_min_1(s)")
   5 function calls in 0.083 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.083    0.083 <string>:1(<module>)
        1    0.083    0.083    0.083    0.083 task_1.py:18(search_max_min_1)
        1    0.000    0.000    0.083    0.083 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run("search_max_min_2(s)")
   5 function calls in 0.254 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.020    0.020    0.254    0.254 <string>:1(<module>)
        1    0.006    0.006    0.234    0.234 task_1.py:30(search_max_min_2)
        1    0.000    0.000    0.254    0.254 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.228    0.228    0.228    0.228 {method 'sort' of 'list' objects}

cProfile.run("search_max_min_3(s)")
   6 function calls in 0.024 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.024    0.024 <string>:1(<module>)
        1    0.000    0.000    0.024    0.024 task_1.py:36(search_max_min_3)
        1    0.000    0.000    0.024    0.024 {built-in method builtins.exec}
        1    0.015    0.015    0.015    0.015 {built-in method builtins.max}
        1    0.009    0.009    0.009    0.009 {built-in method builtins.min}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""