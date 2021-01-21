"""
3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным
образом. Найдите в массиве медиану. Медианой называется элемент ряда, делящий
его на две равные части: в одной находятся элементы, которые не меньше медианы, в
другой — не больше медианы.
Примечание: задачу можно решить без сортировки исходного массива. Но если это
слишком сложно, используйте метод сортировки, который не рассматривался на
уроках (сортировка слиянием также недопустима).
"""
import random


# Нахождение медианы с помощью алгоритма "quickselect", разработанным Тони Хоаром
def quick_select_median(arr):
    if len(arr) % 2 == 1:
        return quick_select(arr, len(arr) // 2)
    else:
        return 0.5 * (quick_select(arr, len(arr) // 2 - 1) + quick_select(arr, len(arr) // 2))


def quick_select(arr, idx):
    if len(arr) == 1:
        assert idx == 0
        return arr[idx]

    pivot = random.choice(arr)

    lows, highs, pivots = [], [], []
    for i in arr:
        if i < pivot:
            lows.append(i)
        elif i > pivot:
            highs.append(i)
        else:
            pivots.append(i)

    if idx < len(lows):
        return quick_select(lows, idx)
    elif idx < len(lows) + len(pivots):
        return pivots[0]
    else:
        return quick_select(highs, idx - len(lows) - len(pivots))


a = [i + 1 for i in range(0, 49)]
random.shuffle(a)

print(f"Исходный массив\n{a}")
mdn = quick_select_median(a)
print(f"Медиана = {mdn}")
