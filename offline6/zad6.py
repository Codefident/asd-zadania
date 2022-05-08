# Piotr Klęp

from math import inf
from zad6testy import runtests
from collections import deque


class Vertex:
    def __init__(self):
        self.d = -1   # distance from vertex s
        self.parents = []   # parents vertex
        self.visited = False


def reverseBFS(G: list, V: list[Vertex], Q: deque, t: int, s: int, d: int):

    Q.clear()

    for v in V[t].parents:
        Q.append(v)

    i = d - 1
    u: int

    while len(Q) > 1 and i > 1:
        u = Q.popleft()

        if V[u].d < i:
            i -= 1

        # paths meet on vertex s - returns None
        if i == 1:
            return None
            
        for v in V[u].parents:
            if v not in Q:
                Q.append(v)
                
    # paths meet before vertex s
    u = V[u].parents[0]
    return (u, V[u].parents[0])


def BFS(G: list, s: int, t: int):

    e = len(G)
    Q = deque()
    V = [Vertex() for _ in range(e)]

    V[s].d = 0
    V[s].visited = True
    Q.appendleft(s)

    shortest_path_length = inf

    while Q:
        u = Q.popleft()

        if V[u].d + 1 > shortest_path_length:
            break

        for v in G[u]:

            # meeting of multiple shortest paths
            if V[v].visited and V[u].d + 1 == V[v].d:
                V[v].parents.append(u)

            # longer path / single shortest path
            elif not V[v].visited:
                V[v].d = V[u].d + 1
                V[v].parents.append(u)
                V[v].visited = True
                    
                if v != t:
                    Q.append(v)
                else:
                    shortest_path_length = V[v].d
                
    print('\nKONIEC, znaleziono najkrotsze sciezki')
    print(V[t].parents)
    
    if V[t].visited:

        if len(V[t].parents) == 1:
            return (t, V[t].parents[0])

        return reverseBFS(G, V, Q, t, s, shortest_path_length)
        
    else:
        return None


def longer(G, s, t):
    return BFS(G, s, t)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(longer, all_tests=True)
