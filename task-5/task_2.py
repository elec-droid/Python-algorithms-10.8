"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При
этом каждое число представляется как массив, элементы которого — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’]
соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
Примечание: Если воспользоваться функциями hex() и/или int() для преобразования
систем счисления, задача решается в несколько строк. Для прокачки алгоритмического
мышления такой вариант не подходит. Поэтому использование встроенных функций
для перевода из одной системы счисления в другую в данной задаче под запретом.
Вспомните начальную школу и попробуйте написать сложение и умножение в столбик.
"""
from collections import deque
from collections import ChainMap

# В решении реализован алгоритм сложения и умножения без явного и косвенного перевода чисел из одной системы счисления
# в другую. Решение основано на заранее известных таблицах арифметических операций над шестнадцатиричными числами.

# Таблица арифметических операций сложения шеснадцатиричных чисел
plus0 = {'0+0': '0', '0+1': '1', '0+2': '2', '0+3': '3', '0+4': '4', '0+5': '5', '0+6': '6', '0+7': '7', '0+8': '8',
         '0+9': '9', '0+A': 'A', '0+B': 'B', '0+C': 'C', '0+D': 'D', '0+E': 'E', '0+F': 'F'}
plus1 = {'1+1': '2', '1+2': '3', '1+3': '4', '1+4': '5', '1+5': '6', '1+6': '7', '1+7': '8', '1+8': '9', '1+9': 'A',
         '1+A': 'B', '1+B': 'C', '1+C': 'D', '1+D': 'E', '1+E': 'F', '1+F': ['1', '0']}
plus2 = {'2+2': '4', '2+3': '5', '2+4': '6', '2+5': '7', '2+6': '8', '2+7': '9', '2+8': 'A', '2+9': 'B', '2+A': 'C',
         '2+B': 'D', '2+C': 'E', '2+D': 'F', '2+E': '10', '2+F': '11'}
plus3 = {'3+3': '6', '3+4': '7', '3+5': '8', '3+6': '9', '3+7': 'A', '3+8': 'B', '3+9': 'C', '3+A': 'D', '3+B': 'E',
         '3+C': 'F', '3+D': '10', '3+E': '11', '3+F': '12'}
plus4 = {'4+4': '8', '4+5': '9', '4+6': 'A', '4+7': 'B', '4+8': 'C', '4+9': 'D', '4+A': 'E', '4+B': 'F', '4+C': '10',
         '4+D': '11', '4+E': '12', '4+F': '13'}
plus5 = {'5+5': 'A', '5+6': 'B', '5+7': 'C', '5+8': 'D', '5+9': 'E', '5+A': 'F', '5+B': '10', '5+C': '11',
         '5+D': '12', '5+E': '13', '5+F': '14'}
plus6 = {'6+6': 'C', '6+7': 'D', '6+8': 'E', '6+9': 'F', '6+A': '10', '6+B': '11', '6+C': '12', '6+D': '13',
         '6+E': '14', '6+F': '15'}
plus7 = {'7+7': 'E', '7+8': 'F', '7+9': '10', '7+A': '11', '7+B': '12', '7+C': '13', '7+D': '14', '7+E': '15',
         '7+F': '16'}
plus8 = {'8+8': '10', '8+9': '11', '8+A': '12', '8+B': '13', '8+C': '14', '8+D': '15', '8+E': '16', '8+F': '17'}
plus9 = {'9+9': '12', '9+A': '13', '9+B': '14', '9+C': '15', '9+D': '16', '9+E': '17', '9+F': '18'}
plusA = {'A+A': '14', 'A+B': '15', 'A+C': '16', 'A+D': '17', 'A+E': '18', 'A+F': '19'}
plusB = {'B+B': '16', 'B+C': '17', 'B+D': '18', 'B+E': '19', 'B+F': '1A'}
plusC = {'C+C': '18', 'C+D': '19', 'C+E': '1A', 'C+F': '1B'}
plusD = {'D+D': '1A', 'D+E': '1B', 'D+F': '1C'}
plusE = {'E+E': '1C', 'E+F': '1D'}
plusF = {'F+F': '1E'}

# Таблица арифметических операций умножения шеснадцатиричных чисел
mul0 = {'0*0': '0', '0*1': '0', '0*2': '0', '0*3': '0', '0*4': '0', '0*5': '0', '0*6': '0', '0*7': '0', '0*8': '0',
        '0*9': '0', '0*A': '0', '0*B': '0', '0*C': '0', '0*D': '0', '0*E': '0', '0*F': '0'}
mul1 = {'1*1': '1', '1*2': '2', '1*3': '3', '1*4': '4', '1*5': '5', '1*6': '6', '1*7': '7', '1*8': '8', '1*9': '9',
        '1*A': 'A', '1*B': 'B', '1*C': 'C', '1*D': 'D', '1*E': 'E', '1*F': 'F'}
mul2 = {'2*2': '4', '2*3': '6', '2*4': '8', '2*5': 'A', '2*6': 'C', '2*7': 'E', '2*8': '10', '2*9': '12', '2*A': '14',
        '2*B': '16', '2*C': '18', '2*D': '1A', '2*E': '1C', '2*F': '1E'}
mul3 = {'3*3': '9', '3*4': 'C', '3*5': 'F', '3*6': '12', '3*7': '15', '3*8': '18', '3*9': '1B', '3*A': '1E',
        '3*B': '21', '3*C': '24', '3*D': '27', '3*E': '2A', '3*F': '2D'}
mul4 = {'4*4': '10', '4*5': '14', '4*6': '18', '4*7': '1C', '4*8': '20', '4*9': '24', '4*A': '28', '4*B': '2C',
        '4*C': '30', '4*D': '34', '4*E': '38', '4*F': '3C'}
mul5 = {'5*5': '19', '5*6': '1E', '5*7': '23', '5*8': '28', '5*9': '2D', '5*A': '32', '5*B': '37', '5*C': '3C',
        '5*D': '41', '5*E': '46', '5*F': '4B'}
mul6 = {'6*6': '24', '6*7': '2A', '6*8': '30', '6*9': '36', '6*A': '3C', '6*B': '42', '6*C': '48', '6*D': '4E',
        '6*E': '54', '6*F': '5A'}
mul7 = {'7*7': '31', '7*8': '38', '7*9': '3F', '7*A': '46', '7*B': '4D', '7*C': '54', '7*D': '5B', '7*E': '62',
        '7*F': '69'}
mul8 = {'8*8': '40', '8*9': '48', '8*A': '50', '8*B': '58', '8*C': '60', '8*D': '68', '8*E': '70', '8*F': '78'}
mul9 = {'9*9': '51', '9*A': '5A', '9*B': '63', '9*C': '6C', '9*D': '75', '9*E': '7E', '9*F': '87'}
mulA = {'A*A': '64', 'A*B': '6E', 'A*C': '78', 'A*D': '82', 'A*E': '8C', 'A*F': '96'}
mulB = {'B*B': '79', 'B*C': '84', 'B*D': '8F', 'B*E': '9A', 'B*F': 'A5'}
mulC = {'C*C': '90', 'C*D': '9C', 'C*E': 'A8', 'C*F': 'B4'}
mulD = {'D*D': 'A9', 'D*E': 'B6', 'D*F': 'C3'}
mulE = {'E*E': 'C4', 'E*F': 'D2'}
mulF = {'F*F': 'E1'}

# Объеденение всех словарей с помощью ChainMap
operations = ChainMap(plus0, plus1, plus2, plus3, plus4, plus5, plus6, plus7, plus8, plus9, plusA, plusB, plusC, plusD,
                      plusE, plusF, mul0, mul1, mul2, mul3, mul4, mul5, mul6, mul7, mul8, mul9, mulA, mulB, mulC, mulD,
                      mulE, mulF)


# Функция арифметической операции над двумя цифрами
def hex_digit_calc(digit1: str, digit2: str, sign: str):
    try:
        return operations[digit1 + sign + digit2]
    except KeyError:
        try:
            return operations[digit2 + sign + digit1]
        except KeyError:
            return None


# Функция сложения двух чисел
def hex_num_sum(number1: deque, number2: deque):
    if len(number2) > len(number1):
        number1, number2 = number2, number1
    result = deque()
    memory = ''
    for _ in range(len(number2)):
        dg1, dg2 = number1.pop(), number2.pop()
        interim_res = hex_digit_calc(dg1, dg2, '+')

        if interim_res is None:
            print("Шестнадцатиричные числа введены некорректно!")
            return None

        # Если на шаге j-1 от суммы получось двухзначное число
        if memory != '':
            # Если на шаге j от суммы получислось двухзначное число
            if len(interim_res) > 1:
                interim_res = interim_res[0] + hex_digit_calc(interim_res[1], memory, '+')
            else:
                interim_res = hex_digit_calc(interim_res, memory, '+')
            memory = ''

        # Сохранение старшего рязряда для шага j+1
        if len(interim_res) > 1:
            result.appendleft(interim_res[1])
            memory = interim_res[0]
        else:
            result.appendleft(interim_res)
    else:
        # Если одного слагаемое больше другого дописываем его остаток к результату
        # с учётом страшего разряда от последней операции в цикле выше
        if len(number1) > 0:
            for _ in range(len(number1)):
                dg1 = number1.pop()
                if memory != '':
                    interim_res = hex_digit_calc(memory, dg1, '+')

                    if len(interim_res) > 1:
                        result.appendleft(interim_res[1])
                        memory = interim_res[0]
                    else:
                        result.appendleft(interim_res)
                        memory = ''
                else:
                    result.appendleft(dg1)
            else:
                if memory != '':
                    result.appendleft(memory)
    return result


# Функция умножения двух чисел
def hex_num_mul(number1: deque, number2: deque):
    if len(number2) > len(number1):
        number1, number2 = number2, number1
    result = []
    total_result = deque()
    memory = ''
    for i in range(len(number2)):
        dg2 = number2.pop()
        nb = deque(number1)
        result.append(deque('0' * i))

        for j in range(len(nb)):
            dg1 = nb.pop()
            interim_res = hex_digit_calc(dg1, dg2, '*')

            if interim_res is None:
                print("Шестнадцатиричные числа введены некорректно!")
                return None

            # Если на шаге j-1 от произведения получось двухзначное число
            if memory != '':
                # Если на шаге j от произведения получислось двухзначное число
                if len(interim_res) > 1:
                    loc_mem = hex_digit_calc(interim_res[1], memory, '+')

                    # Если сумма старшего разряда шага j-1 и младшего разряда j даёт двухзначное число
                    if len(loc_mem) > 1:
                        interim_res = hex_digit_calc(interim_res[0], loc_mem[0], '+') + loc_mem[1]
                    else:
                        interim_res = interim_res[0] + loc_mem
                # Если на шаге j от произведения получилось цифра
                else:
                    loc_mem = hex_digit_calc(interim_res, memory, '+')

                    # Если сумма старшего разряда шага j-1 и младшего разряда j даёт двухзначное число
                    if len(loc_mem) > 1:
                        interim_res = loc_mem[0] + loc_mem[1]
                    else:
                        interim_res = loc_mem
                memory = ''

            # Сохранение старшего рязряда для шага j+1
            if len(interim_res) > 1:
                result[i].appendleft(interim_res[1])
                memory = interim_res[0]
            else:
                result[i].appendleft(interim_res)
        else:
            if memory != '':
                result[i].appendleft(memory)
                memory = ''
            total_result = hex_num_sum(total_result, result[-1])
    return total_result


# Для упрощение принято, что пользователь адекватен и вводит корректные данные
# Получение данных с небольшими проверками
in_str = input("Введите операцию над двумя шестнадцатиричными числами\n"
               "Шестнадцатиричные числа состоят только из цифр от 0 до 9 и заглавных букв латинского алфавита от A до F"
               "Доступны операции сложения и умножения. Выражение должно быть вида: 24FA + CE29\n")
while True:
    temp = in_str.split(' ')
    if len(temp) == 3:
        sign = temp[1]
        operand1 = deque(temp[0])
        operand2 = deque(temp[2])
        break

print('*' * 50)
if sign == '+':
    print(''.join(hex_num_sum(operand1, operand2)))
elif sign == '*':
    print(''.join(hex_num_mul(operand1, operand2)))
else:
    print(f"Введён недопустимый знак операции {sign}. Доступно только + или *")
