# dag - directed acyclic graph
# wszystkie krawędzie mają wskazywać "z lewa na prawo"

# DFS po krawędziach
# gdy kończymy odwiedzać sąsiadów to prependujemy wierzchołek na początek listy

# https://eduinf.waw.pl/inf/alg/001_search/0137.php


def topSort_DFS(G: list):

    n = len(G)
    visited = [False] * n
    output = [None] * n
    output_i = n - 1

    def DFSVisit(v: int):
        nonlocal output_i
        visited[v] = True

        for u in G[v]:
            if not visited[u]:
                DFSVisit(u)

        output[output_i] = v
        output_i -= 1

    for v in range(n):
        if not visited[v]:
            DFSVisit(v)

    return output


G = [
    [2],  # 0
    [0, 2],  # 1
    [],  # 2
    [0, 1, 4],  # 3
    [1, 2],  # 4
    [0, 4]  # 5
]

print(topSort_DFS(G))
