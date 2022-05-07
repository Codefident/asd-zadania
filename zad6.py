# Piotr Klęp

from zad6testy import runtests
from collections import deque


class Vertex:
    def __init__(self, i):
        self.i = i   # number/index of vertex
        self.d = []   # distance from vertex s
        self.parents = []   # parents vertex
        self.visited = False


def BFS(G, s, t):

    e = len(G)
    Q = deque()
    V = []

    for i in range(e):
        V.append(Vertex(i))

    V[s].d.append(0)
    V[s].visited = True
    Q.appendleft(s)

    while Q:
        u = Q.popleft()
        for v in G[u]:

            if not V[v].visited:
                V[v].visited = True
                V[v].d.append(V[u].d[0] + 1)
                V[v].parents.append(u)

                if v != t:
                    Q.append(v)

            else:
                V[v].d.append(V[u].d[0] + 1)
                V[v].parents.append(u)

    if V[t].visited:
        i = t
        while i != s:
            if len(V[i].parents) > 1:
                for d in V[i].d:
                    if d > V[i].d[0]:
                        return (i, V[i].parents[0])
            i = V[i].parents[0]
    else:
        return None


def longer(G, s, t):
    return BFS(G, s, t)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(longer, all_tests=True)
