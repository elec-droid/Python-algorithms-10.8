"""
4. Определить, какое число в массиве встречается чаще всего.
"""
from random import randrange

a = [randrange(1, 10) for _ in range(20)]
print(f"Исходный массив целых чисел {a}")

com = [0, 0]
for itr in set(a):
    if com[1] < a.count(itr) and a.count(itr) > 1:
        com[0], com[1] = itr, a.count(itr)

if not com[0]:
    print(f"Все числа встречаются одинаковое количество раз")
else:
    print(f"Наиболее часто встречающееся число {com[0]} встречается {com[1]} раз")
