"""
2. Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно
возвращал список вершин, которые необходимо обойти.
"""
from collections import deque


q = [  # 0  1  2  3  4  5  6  7
        [0, 0, 1, 1, 9, 0, 0, 0],   # 0
        [0, 0, 9, 4, 0, 0, 7, 0],   # 1
        [0, 9, 0, 0, 3, 0, 6, 0],   # 2
        [0, 0, 0, 0, 0, 0, 0, 0],   # 3
        [0, 0, 0, 0, 0, 0, 1, 0],   # 4
        [0, 0, 0, 0, 0, 0, 5, 0],   # 5
        [0, 0, 7, 0, 8, 1, 0, 0],   # 6
        [0, 0, 0, 0, 0, 1, 2, 0],   # 7
]


def dijkstra(graph, start):
    length = len(graph)
    is_visited = [False] * length
    cost = [float('inf')] * length
    cur_vertex = start

    path = [deque() for _ in range(length)]
    parent = [-1] * length
    parent[cur_vertex] = 0
    cost[cur_vertex] = 0
    min_cost = 0

    while min_cost < float('inf'):
        is_visited[cur_vertex] = True

        for i, vertex in enumerate(graph[cur_vertex]):
            if vertex != 0 and not is_visited[i]:
                if cost[i] > cost[cur_vertex] + vertex:
                    cost[i] = cost[cur_vertex] + vertex
                    parent[i] = cur_vertex

        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                cur_vertex = i

    # запись списка вершин кратчайшего пути
    for i, itr in enumerate(path):
        j = int(i)
        while parent[j] != 0:
            if parent[j] < 0:
                path[i].clear()
                path[i].appendleft(float('inf'))
                break

            path[i].appendleft(j)
            j = parent[j]
        else:
            path[i].appendleft(j)
            if start == 0:
                path[i].appendleft(0)

    return cost, path


c, p = dijkstra(q, 0)

print(c)
print(*p, sep='\n')
