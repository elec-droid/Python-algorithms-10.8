"""
2. Написать два алгоритма нахождения i-го по счёту простого числа. Функция
нахождения простого числа должна принимать на вход натуральное и возвращать
соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых
уроков. Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
Второй — без использования «Решета Эратосфена».
Примечание. Вспомните классический способ проверки числа на простоту.
"""
import math
import cProfile
# import timeit


# Поиск i-го по счёту простого числа, алгоритм "Решето Эратосфена"
# Реализация, мягко говоря, не самая быстрая, прошу сильно не пинать
def sieve_erat(n: int):
    if n < 3:
        return n
    else:
        # если искомое число не 3-е и дальше по порядку
        prime = []
        # начальные границы
        start_num = 2
        stop_num = 100

        while len(prime) < n:
            s = list(range(start_num, stop_num))
            # Если Отсев по уже найденными простыми числами
            # Число не является простым если имеет хотя бы один делитель из ряда простых чисел
            if len(prime) > 0:
                for itr in prime:
                    # определение ближайшего кратного простого числа в начале последовательности s
                    _ = start_num if start_num % itr == 0 else itr + itr * (start_num // itr)
                    for jtr in range(_, stop_num, itr):
                        s[jtr - start_num] = 0

            # Отсев остальных значений
            for itr in s:
                if itr != 0:
                    if s[itr - start_num] != 0:
                        for jtr in range(2 * itr, stop_num, itr):
                            s[jtr-start_num] = 0
            # для удаления нулей из списка
            prime.extend(list(set(s)))
            # для предотвращения нарушения корректной последовательности после приведения к set
            prime.sort()
            # удаления '0'
            prime.pop(0)
            # задание границ следующего диапазона поиска
            start_num, stop_num = stop_num, stop_num + 1000
        return prime[n-1]


# Поиск i-го по счёту простого числа, простая проверка
def sieve_simple(n: int):
    if n < 3:
        return n
    else:
        prime = [2, 3]
        next_num = 5
        while len(prime) < n:
            for i in range(3, int(math.sqrt(next_num) + 1)):
                if next_num % i == 0:
                    break
            else:
                prime.append(next_num)
            # всё чётные числа являются составными
            next_num += 2
        return prime[-1]

# cProfile.run("sieve_simple(100000)")

"""
Анализ времени работы реализованных алгоритмов показывает, что вариант с перебором делителей
работает эффективнее. Оба алгоритма имеют сложность логарифмическу сложность O(log n)

-- Сводные данные по времени работы алгоритмов, измеренному с помощью timeit
-- Измерения проводились для 500 повторений, а последний - для 100
i-е         sieve_erat   sieve_simple
10          12.4 usec    12.8 usec
100         181  usec    147  usec
1000        2.28 msec    3.88 msec
10000       140  msec    110  msec
50000       3.56 sec     1.39 sec


# ######## Измерение скорости алгоритмов поиск 10-го простого числа ########
$ python -m timeit -n 500 -r 2 -s "import task_2" "task_2.sieve_erat(10)"
1000 loops, best of 10: 12.4 usec per loop
$ python -m timeit -n 500 -r 2 -s "import task_2" "task_2.sieve_simple(10)"
500 loops, best of 2: 12.8 usec per loop

# ######## Измерение скорости алгоритмов поиск 100-го простого числа ########
$ python -m timeit -n 500 -r 2 -s "import task_2" "task_2.sieve_erat(100)"
500 loops, best of 2: 181 usec per loop
$ python -m timeit -n 500 -r 2 -s "import task_2" "task_2.sieve_simple(100)"
500 loops, best of 2: 147 usec per loop

# ######## Измерение скорости алгоритмов поиск 1000-го простого числа ########
$ python -m timeit -n 500 -r 2 -s "import task_2" "task_2.sieve_erat(1000)"
500 loops, best of 2: 2.28 msec per loop
$ python -m timeit -n 500 -r 2 -s "import task_2" "task_2.sieve_simple(1000)"
500 loops, best of 2: 3.88 msec per loop

# ######## Измерение скорости алгоритмов поиск 10000-го простого числа ########
$ python -m timeit -n 500 -r 2 -s "import task_2" "task_2.sieve_erat(10000)"
500 loops, best of 2: 140 msec per loop
$ python -m timeit -n 500 -r 2 -s "import task_2" "task_2.sieve_simple(10000)"
500 loops, best of 2: 110 msec per loop

# ######## Измерение скорости алгоритмов поиск 50000-го простого числа ########
$ python -m timeit -n 100 -r 1 -s "import task_2" "task_2.sieve_erat(50000)"
100 loops, best of 1: 3.56 sec per loop
$ python -m timeit -n 100 -r 1 -s "import task_2" "task_2.sieve_simple(50000)"
100 loops, best of 1: 1.39 sec per loop

# cProfile.run("sieve_erat(100000)")
   6510 function calls in 15.929 seconds
   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001   15.929   15.929 <string>:1(<module>)
        1   15.521   15.521   15.929   15.929 task_2.py:18(sieve_erat)
        1    0.000    0.000   15.929   15.929 {built-in method builtins.exec}
     2603    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     1301    0.002    0.000    0.002    0.000 {method 'extend' of 'list' objects}
     1301    0.013    0.000    0.013    0.000 {method 'pop' of 'list' objects}
     1301    0.392    0.000    0.392    0.000 {method 'sort' of 'list' objects}

# cProfile.run("sieve_simple(100000)")
   1399709 function calls in 4.350 seconds
   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001    4.350    4.350 <string>:1(<module>)
        1    4.260    4.260    4.349    4.349 task_2.py:57(sieve_simple)
        1    0.000    0.000    4.350    4.350 {built-in method builtins.exec}
   649854    0.036    0.000    0.036    0.000 {built-in method builtins.len}
   649853    0.045    0.000    0.045    0.000 {built-in method math.sqrt}
    99998    0.008    0.000    0.008    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""