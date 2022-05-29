from zad7testy import runtests


def DFSVisit(G, u, time, visited, parents, parent=None):
    time += 1
    visited[u] = True

    for v in G[u][1]:
        pass


def DFS(G: list):
    n = len(G)
    visited = [False] * n
    parents = [None] * n
    time = 1

    for u in range(n):
        if not visited[u]:
            DFSVisit(G, u, time, visited, parents)


def droga(G):
    # tu prosze wpisac wlasna implementacje
    return None


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(droga, all_tests=False)
