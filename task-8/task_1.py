"""
1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по
одному разу). Сколько рукопожатий было?
Примечание. Решите задачу при помощи построения графа.
"""


def handshake_counter(graph, is_double_handshake=True):
    length = len(graph)
    is_visited = [False] * length
    counter = 0

    for i in range(length):
        for j in range(length):
            if is_double_handshake:
                if graph[i][j]:
                    counter += 1
            else:
                if graph[i][j] and not is_visited[j]:
                    counter += 1

        is_visited[i] = True
    return counter


# Решение с использованием матрицы смежности
n_friends = int(input(f"Сколько друзей встретилось на улице? "))
in_graph = [[0 if j == i else 1 for j in range(n_friends)] for i in range(n_friends)]

print("Граф")
print(*in_graph, sep="\n")
print()
print(f"Было {handshake_counter(in_graph)} рукопожатий \n"
      f"(если учитывать 'двойные' - когда 1 жмет руку 2, а потом 2 жмет руку 1)")
print('-' * 50)
print(f"Было {handshake_counter(in_graph, False)} рукопожатий\n"
      f"(если НЕ учитывать 'двойные' - когда 1 жмет руку 2, и это считается за рукопожатие 2 - 1)")

