"""
4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество
элементов (n) вводится с клавиатуры.
"""

print("Введите количество элементов последовательности")
n = int(input())
S = ((-0.5) ** n - 1)/-1.5
print(f"Сумма первых {n} членов последовательности равна {S}")
