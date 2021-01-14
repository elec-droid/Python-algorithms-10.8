"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за четыре квартала для каждого предприятия. Программа должна
определить среднюю прибыль (за год для всех предприятий) и отдельно вывести
наименования предприятий, чья прибыль выше среднего и ниже среднего.
"""
from collections import defaultdict


# Проверка на является ли строка вещественным числов (в том числе натуральным)
def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


# Получение данных с небольшими проверками
in_str = input("Введите количество предприятий: ")
company = 0
def_dict = defaultdict(list)
while not in_str.isdigit():
    print("Число компаний должно быть целым и больше 0")
    in_str = input("Введите количество предприятий: ")
else:
    company = int(in_str)

print(f"Для каждого из {company} предприятий введите название и прибыль за четыре квартала\n"
      f"Данные должны передаваться последовательно в одной строке. Название компании отделяется ':', прибыль - "
      f"пробелом, например\n Красный котельник: 200.2 300 120.5 600")
for i in range(company):
    while True:
        in_str = input(f"Предприятие № {i + 1} - ")
        t_name = in_str.split(':')
        if len(t_name) == 2:
            t_profit = t_name[1].split(' ')
            profit = [float(itr) for itr in t_profit if isfloat(itr)]
            if len(profit) == 4:
                def_dict[t_name[0]] = profit
                break
        print("Нарушена структура входных данных, попробуйте ещё раз")

# Подсчёт средней прибыли для каждого из предприятий и общей средней прибыли
total_mean = 0
for i, v in def_dict.items():
    mean = sum(v) / 4
    total_mean += mean
    def_dict[i].append(mean)
total_mean /= company

# распределение по группам
def_dict_mle = defaultdict(list)
for i, v in def_dict.items():
    if v[-1] > total_mean:
        def_dict_mle['Компании с прибылью больше среднего'].append(i)
    elif v[-1] < total_mean:
        def_dict_mle['Компанни с прибылью меньше среднего'].append(i)
    else:
        def_dict_mle['Компании с прибылью равной среднему'].append(i)

# Вывод результатов расчёта
print(f"Среднее значение прибыли всех компаний {total_mean}")
for i, v in def_dict_mle.items():
    print(i)
    for itr in v:
        print(f"{itr} - средняя прибыль {def_dict[itr][-1]:.2f}")
