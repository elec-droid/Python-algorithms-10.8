"""
3. Написать программу, которая генерирует в указанных пользователем границах:
    a. случайное целое число,
    b. случайное вещественное число,
    c. случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона. Например, если надо получить случайный символ
от 'a' до 'f', то вводятся эти символы. Программа должна вывести на экран любой символ алфавита от 'a' до 'f'
включительно.
"""

from random import randint
from random import uniform

print("Введите границы диапазона")
a = input("Введите левую границу: ")
b = input("Введите правую границу: ")

if a.isalpha() and b.isalpha():
    a_code, b_code = ord(a.lower()), ord(b.lower())
    if b_code < a_code:
        a_code, b_code = b_code, a_code
    c = chr(randint(a_code, b_code))
elif a.isdecimal() and b.isdecimal():
    a, b = int(a), int(b)
    if b < a:
        a, b = b, a
    c = randint(a, b)
else:
    a, b = float(a), float(b)
    if b < a:
        a, b = b, a
    c = uniform(a, b)

print(f"Случайное значение: {c}")
