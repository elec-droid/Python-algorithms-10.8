"""
2. Закодируйте любую строку по алгоритму Хаффмана.
"""
from collections import Counter


class Node:
    def __init__(self, value, left=None, right=None):
        self.right = right
        self.left = left
        self.value = value


def get_code(root, codes=dict(), code=''):

    if root is None:
        return

    if isinstance(root.value, str):
        codes[root.value] = code
        return codes

    get_code(root.left, codes, code + '0')
    get_code(root.right, codes, code + '1')

    return codes


def get_tree(string):
    string_count = Counter(string)

    if len(string_count) <= 1:
        node = Node(None)

        if len(string_count) == 1:
            node.left = Node([key for key in string_count][0])
            node.right = Node(None)

        string_count = {node: 1}

    while len(string_count) != 1:
        node = Node(None)
        spam = string_count.most_common()[:-3:-1]

        if isinstance(spam[0][0], str):
            node.left = Node(spam[0][0])
        else:
            node.left = spam[0][0]

        if isinstance(spam[1][0], str):
            node.right = Node(spam[1][0])
        else:
            node.right = spam[1][0]

        del string_count[spam[0][0]]
        del string_count[spam[1][0]]
        string_count[node] = spam[0][1] + spam[1][1]

    return [key for key in string_count][0]


def coding(string, codes):
    result = ''

    for symbol in string:
        result += codes[symbol]

    return result


def decoding(string, codes):
    result = ''
    i = 0

    while i < len(string):
        for c in codes:
            if string[i:].find(codes[c]) == 0:
                result += c
                i += len(codes[c])

    return result


in_str = input('Введите строку для сжатия: ')
if in_str == '':
    in_str = "Здесь будет моя строка потому что Вы не ввели нечего"
    print(in_str)

code = get_code(get_tree(in_str))
coding_str = coding(in_str, code)
decoding_str = decoding(coding_str, code)
print(f"Кодовый словарь по алгоритму Хаффмана: \n{code}\n"
      f"Код строки по алгоритму Хаффмана: \n{coding_str}\n"
      f"Строка, декодированная их исходной: \n{decoding_str}")

assert in_str == decoding_str, "Ошибка при кодировании и декодирование строки по алгоритму Хаффмана"
