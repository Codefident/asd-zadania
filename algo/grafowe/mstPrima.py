# Algorytm Prima znajdowania MST

# 1. start z wierzchołka s
# 2. umieszczamy wszystkie wierzchołki w kolejce prioriytetowej z wagą inf (tego technicznie nie robimy)
# 3. waga s = 0 (szczyt kolejki)
# 4. dopóki są wierzchołki w kolejce:
#   4.1 wyjmij wierzchołek t o min. wadze
#   4.2 dla każdej krawędzi {t, u}:
#       - jeśli waga u >= w{t, u}, to zamień wagę u na wagę w{t, u}
#       i uaktualnij parent

from queue import PriorityQueue


def prim(G: list, s: int):

    n = len(G)
    parent = [None] * n
    weights = [float('inf')] * n
    visited = [False] * n

    PQ = PriorityQueue()

    PQ.put((0, s))
    weights[s] = 0

    while not PQ.empty():
        p, t = PQ.get()

        visited[t] = True

        for u in range(n):
            weight = G[t][u]

            if (weight < weights[u]
                    and weight > 0
                    and not visited[u]):
                parent[u] = t
                weights[u] = weight
                PQ.put((weight, u))

    print(weights)
    print(parent)
    letters = ['s', 'a', 'b', 'c', 'd', 'e']
    wyklad = True

    for i in range(n):
        if i == s:
            continue
        if wyklad:
            print(letters[parent[i]], '<= (', weights[i], ') =', letters[i])
        else:
            print(i, '= (', weights[i], ') =>', parent[i])


G = [
    [0, 1, 3, 0, 0, 0],
    [1, 0, 0, 4, 2, 0],
    [3, 0, 0, 1, 2, 0],
    [0, 4, 1, 0, 0, 1],
    [0, 2, 2, 0, 0, 3],
    [0, 0, 0, 1, 3, 0]
]

prim(G, 0)
