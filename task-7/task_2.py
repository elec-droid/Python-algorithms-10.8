"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и
отсортированный массивы.
"""
import random


def merge_sort(array: list):
    if len(array) < 2:
        return array
    else:
        middle = len(array) // 2
        left = merge_sort(array[:middle])
        right = merge_sort(array[middle:])
        return merge(left, right)


def merge(left, right):
    result = []
    l, r = 0, 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    while l < len(left):
        result.append(left[l])
        l += 1
    while r < len(right):
        result.append(right[r])
        r += 1
    return result


a = [random.randint(0, 50) / random.randint(1, 10) for i in range(0, 50)]
# a = [i for i in range(0, 50)]
random.shuffle(a)

print(f"Исходный массив\n{a}")
a = merge_sort(a)
print(f"Отсортированный массив\n{a}")
