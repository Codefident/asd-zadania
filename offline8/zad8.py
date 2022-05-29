# Piotr Klęp

# === ZŁOŻONOŚĆ ===
# obliczeniowa: O( E + ElogE + 2E(V + E) )
# pamięciowa:   O( E + VE )

# === OPIS DZIAŁANIA ===

# 1. zapisuję w liście E wszystkie krawędzie posortowane rosnąco wg długości.
# 2. wrzucam do grafu (lista kolejek(!) sąsiadów) pierwsze |V| - 1 krawędzi z tej listy.
# 3. pętla:
#   3a. jeśli graf jest spójny -> usuwamy najmniejszą krawędź z grafu
#   3b. jeśli graf niespójny -> dodajemy do grafu kolejną krawędź z listy
# 4. koniec pętli gdy ani nie wrzuciliśmy krawędzi ani nie usunęliśmy

# spójność grafu sprawdzam BFSem


from collections import deque
from math import ceil, sqrt
from zad8testy import runtests


def d(a, b):
    x = b[0] - a[0]
    y = b[1] - a[1]
    return ceil(sqrt(x**2 + y**2))


# BFS tylko z kontrolą 'wizyt'
def isConnected(G):

    for neighbours in G:
        if len(neighbours) == 0:
            return False

    n = len(G)
    visited = [False] * n
    visited[0] = True
    Q = deque()
    Q.appendleft(0)

    while Q:
        u = Q.popleft()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                Q.append(v)

    if False in visited:
        return False
    return True


def highway(A):

    n = len(A)
    days = float('inf')

    # lista z krawedziami
    E = []
    for i in range(n):
        for j in range(i + 1, n):
            E.append((i, j, d(A[i], A[j])))

    # sortowanie krawedzi
    E.sort(key=lambda x: x[2])

    # macierz
    G = [deque() for _ in range(n)]

    for i in range(n - 1):
        G[E[i][0]].append(E[i][1])
        G[E[i][1]].append(E[i][0])

    # na poczatku w grafie mamy n-1 najmniejszych wierzcholkow
    i = 0
    j = n - 2

    while True:

        changed = False

        if isConnected(G):
            diff = E[j][2] - E[i][2]
            if diff < days:
                days = diff

            G[E[i][0]].popleft()
            G[E[i][1]].popleft()
            i += 1
            changed = True

        elif j < len(E) - 1:
            j += 1
            G[E[j][0]].append(E[j][1])
            G[E[j][1]].append(E[j][0])
            changed = True

        if not changed:
            return days


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(highway, all_tests=True)
