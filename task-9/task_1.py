"""
1. Определение количества различных подстрок с использованием хеш-функции.
Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
Примечания:
* в сумму не включаем пустую строку и строку целиком;
* без использования функций для вычисления хэша (hash(), sha1() или любой другой
из модуля hashlib задача считается не решённой.
"""
from hashlib import sha1


# Своя простая хеш-функция
def my_hash(s: str):
    result = 0
    length = len(s)

    for i, letter in enumerate(s):
        result += ord(letter) * 10 ^ (length - i)

    return result


# Поиск подстроки с помощью алгоритма Рабина - Карпа
def str_entry(s: str, subs: str, pos=0):
    assert len(s) > 0, "Строка не может быть пустой"
    assert 0 < len(subs) <= len(subs), "Подстрока не может быть пустой и боль чем исходная строка"
    assert pos < len(s), f"Позиция начала поиска {pos} должна входить в строку {s}"

    len_sub = len(subs)
    h_subs = my_hash(subs)

    for i in range(pos, len(s) - len_sub + 1):
        if h_subs == my_hash(subs):

            if s[i:i + len_sub] == subs:
                return i

    return -1


def entry_count(s: str, sep=None, is_subs=False):
    length = len(s)
    result = []

    if sep is None:     # Для определения количества вхождений каждой из всех возможных подстрок
        subs = set()

        for i in range(length):
            for j in range(i + 1, length):
                subs.add(s[i:j])

        if ' ' in subs:
            subs.remove(' ')

        subs = list(subs)
        subs.sort(key=len)
    elif is_subs:       # Для поиска конкретной подстроки
        subs = sep
    else:               # Для поиска подстрок, сформированных из исходной по заданному разделителю
        subs = s.split(sep)

    for sub in subs:
        pos = 0
        loc_counter = 0

        while pos < length:
            pos = str_entry(s, sub, pos)

            if pos < 0:
                pos = length
            else:
                loc_counter += 1
                pos = pos + len(sub) if pos + len(sub) < length else length

        result.append((sub, loc_counter))

    return result


in_str = input("Введите какую-нибудь строку\n")
if in_str == '':
    in_str = "Здесь будет моя строка потому что Вы не ввели нечего"
    print(in_str)

entries = entry_count(in_str)
for itr in entries:
    if itr[1] > 1:
        print(f"'{itr[0]}'", itr[1], sep=' ' * (8 - len(itr[0])))
else:
    print(f"Из исходной строки всего было сформировано {len(entries)} подстрок")
    print("Все остальные возможные подстроки входят в исходную строку не более 1 раза")
