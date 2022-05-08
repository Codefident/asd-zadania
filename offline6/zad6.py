# Piotr Klęp

from zad6testy import runtests
from collections import deque


class Vertex:
    def __init__(self, i):
        self.i = i   # number/index of vertex
        self.d = -1   # distance from vertex s
        self.parents = []   # parents vertex
        self.visited = False
        self.lastVisited = -1


def BFS(G, s, t):

    e = len(G)
    Q = deque()
    V = []

    for i in range(e):
        V.append(Vertex(i))

    V[s].d = 0
    V[s].visited = True
    Q.appendleft(s)

    shortest_path_length = -1

    while Q and shortest_path_length < 0:
        u = Q.popleft()

        for v in G[u]:

            # najkrótsze ścieżki spotykają się
            if V[v].visited and V[u].d + 1 == V[v].d:
                V[v].parents.append(u)

            # jesteśmy na dłuższej ścieżce
            elif not V[v].visited:
                V[v].d = V[u].d + 1
                V[v].parents.append(u)
                V[v].visited = True
                    
                if v != t:
                    Q.append(v)
                else:
                    shortest_path_length = V[v].d
                
    print()
    if V[t].visited:
        return None
        # i = t
        # while i != s:
        #     if len(V[i].parents) > 1:
        #         for d in V[i].d:
        #             if d > V[i].d[0]:
        #                 return (i, V[i].parents[0])
        #     i = V[i].parents[0]
    else:
        return None


def longer(G, s, t):
    return BFS(G, s, t)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(longer, all_tests=True)
