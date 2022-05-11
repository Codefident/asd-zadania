# Piotr Klęp

# złożoność: O(V + E + k)
# k - długość najkrótszej ścieżki

# Najpierw algorytmem BFS przeszukuję graf, z tą różnicą, że w
# wierzchołkach zapisuję parentów ze wszystkich najkrótszych ścieżek
# jeżeli w tym wierzchołku się spotykają.


# Następnie po odnalezieniu ścieżek (bądź też nie):

# - zwracam None jeśli nie odnaleziono ścieżki

# - zwracam docelowy wierzchołek oraz jego parenta jeżeli
#   ma on tylko jednego parenta

# - zwracam wynik funkcji reverseBFS(), która:
#       kroczy wstecz po parentach do momentu, aż wszystkie
#       najkrósze ścieżki spotkają się w jednym miejscu niebędącym
#       wierzchołkiem początkowym s. Wtedy zwracam ten wierzchołek oraz
#       jego parenta


from math import inf
from zad6testy import runtests
from collections import deque


class Vertex:
    def __init__(self):
        self.d = -1   # distance from vertex s
        self.parents = []   # parents vertex
        self.visited = False


def reverseBFS(G: list, V: list[Vertex], Q: deque, t: int, d: int):

    Q.clear()

    for v in V[t].parents:
        Q.append(v)

    i = d - 1
    u: int

    while i > 1:

        if len(Q) == 1:
            u = Q.popleft()

            # same vertex AND same following path, preventing situation when paths spread out right after meeting at a vertex
            if len(V[u].parents) == 1:
                break
        else:
            u = Q.popleft()

        if V[u].d < i:
            i -= 1

        # paths meet at vertex s - returns None
        if i == 1:
            return None

        for v in V[u].parents:
            if v not in Q:
                Q.append(v)

    # paths meet before vertex s
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

    if V[t].visited:
        if len(V[t].parents) == 1:
            return (t, V[t].parents[0])
        return reverseBFS(G, V, Q, t, shortest_path_length)

    else:
        return None


def longer(G, s, t):
    return BFS(G, s, t)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(longer, all_tests=True)
