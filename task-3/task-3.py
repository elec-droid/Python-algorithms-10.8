"""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
from random import randrange

a = [randrange(1, 100) for _ in range(10)]
print(f"Исходный массив целых чисел {a}")

max_i = [a[0], 0]
min_i = [a[0], 0]
for i in range(0, len(a)):
    if max_i[0] < a[i]:
        max_i[0], max_i[1] = a[i], i
    if min_i[0] > a[i]:
        min_i[0], min_i[1] = a[i], i

a[max_i[1]], a[min_i[1]] = a[min_i[1]], a[max_i[1]]
print(f"Массив целых чисел после перестановки максимального и минимального {a}")
