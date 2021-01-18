"""
Для оценки «Отлично» необходимо выполнить все требования, указанные в задании и примечаниях.
1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
    a. выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
    b. написать 3 варианта кода (один у вас уже есть);
    c. проанализировать 3 варианта и выбрать оптимальный;
    d. результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев в файл
        с кодом. Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
    e. написать общий вывод: какой из трёх вариантов лучше и почему.
Надеемся, что вы не испортили программы, добавив в них множество sys.getsizeof после каждой переменной,
а проявили творчество, фантазию и создали универсальный код для замера памяти.
"""
import sys
from random import randrange


# Функция из урока для подсчёта занимаемой памяти
def show_size(x, level=0):
    total_size = sys.getsizeof(x)
    # print('\t' * level, f"type= {x.__class__}, size= {sys.getsizeof(x)}, object= {x}")

    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                total_size += show_size(xx, level + 1)
        elif not isinstance(x, str):
            for xx in x:
                total_size += show_size(xx, level + 1)

    return total_size


# Оценивается алгоритм из задачи № 3 к уроку № 3: В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.
def search_max_min_1(*a: list):
    a = [randrange(1, 1000) for _ in range(1000)]
    max_i = [a[0], 0]
    min_i = [a[0], 0]
    for i in range(0, len(a)):
        if max_i[0] < a[i]:
            max_i[0], max_i[1] = a[i], i
        if min_i[0] > a[i]:
            min_i[0], min_i[1] = a[i], i

    print(f"search_max_min_1 {(show_size(a) + show_size(max_i) + show_size(min_i))/1024:.2f}  kb")
    return max_i[0], min_i[0]


def search_max_min_2(*a: list):
    a = [randrange(1, 1000) for _ in range(1000)]
    _ = a[:]
    _.sort()
    print(f"search_max_min_2 {(show_size(a) + show_size(_))/1024:.2f} kb")
    return _[-1], _[0]


def search_max_min_3(*a: list):
    a = [randrange(1, 1000) for _ in range(1000)]
    print(f"search_max_min_3 {show_size(a)/1024:.2f} kb")
    return max(a), min(a)


print(sys.platform, sys.version)
print("*" * 50)
search_max_min_1()
search_max_min_2()
search_max_min_3()

"""
Не осилил трассировку памяти, поэтому сделал наиболее очевидным способом

linux 3.8.5 (default, Jul 28 2020, 12:59:40) 
[GCC 9.3.0]
**************************************************
search_max_min_1 36.40  kb
search_max_min_2 71.36 kb
search_max_min_3 36.15 kb

search_max_min_3 занимает меньше всего памяти; search_max_min_1 - памяти на две целочисленные переменный больше;
search_max_min_2 - памяти больше в 2 раза из-за создания копии списка
"""