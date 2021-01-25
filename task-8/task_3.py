"""
3. Написать программу, которая обходит не взвешенный ориентированный граф без
петель, в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First
Search). Примечания:
a. граф должен храниться в виде списка смежности;
b. генерация графа выполняется в отдельной функции, которая принимает на вход
число вершин.
"""


# Генерация не взвешенного ориентированного графа без петель по количеству вершин
def gen_graph(n_vertex: int):
    graph = {}

    for i in range(n_vertex):
        graph.setdefault(i)
        if i < 2 * n_vertex // 3:
            graph[i] = tuple(
                j for j in range(n_vertex) if j != i and (graph[j].count(i) == 0 if j in graph.keys() else True)
            )
        else:
            graph[i] = tuple(
                j for j in range(n_vertex) if j != i and (graph[j].count(i-1) == 0 if j in graph.keys() else True)
            )

    return graph


# Алгоритм обхода графа в глубину
# Находится первый попавшийся путь до целевой вершины или возвращается False
def dfs(graph, start, end, is_visited=None, path=None):
    # Создание переменных в начале рекурсии
    if is_visited is None:
        is_visited = [False] * len(graph)
    if path is None:
        path = [start]

    # Проверка условий возврата
    if start == end:
        return True, path
    elif is_visited[start]:
        path.pop()
        return False, path

    is_visited[start] = True

    # Перебор соседних вершин
    for ngb in graph[start]:
        if not is_visited[ngb]:
            path.append(ngb)
            return dfs(graph, ngb, end, is_visited, path)


g = gen_graph(7)
print("Исходный граф:")
for i, k in g.items():
    print(i, ':', *k)
print('-' * 50)
print(dfs(g, 5, 3))
