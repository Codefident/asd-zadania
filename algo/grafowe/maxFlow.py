# problem maksymalnego przepływu
# metoda Forda-Fulkersona / algorytm Edmondsa-Karpa

from collections import deque


def bfs(C, F, C_res, s, t):
    n = len(C)
    parent = [-1] * n  # parenty
    Q = deque()

    Q.append(s)
    parent[s] = -2  # -2 ponieważ nie bierzemy pod uwagę źródła

    while Q:
        v = Q.popleft()

        # sąsiedzi wierzchołka v
        for u in range(n):

            # obliczamy możliwą do wykorzystania przepustowość dla krawędzi w sieci rezydualnej ze wzoru
            # c(v, u) - f(v, u)
            res_capacity = C[v][u] - F[v][u]

            # wykonujemy jeżeli daną krawędzią można jeszcze puścić trochę wody/paliwa
            # oraz jeżeli nie odwiedziliśmy jeszcze danego wierzchołka
            if res_capacity > 0 and parent[u] == -1:
                parent[u] = v

                # bierzemy mniejszą przepustowość (dla obecnego wierzchołka lub tę z parenta)
                # chodzi o zależność większej przepustowości od mniejszej
                C_res[u] = min(res_capacity, C_res[v])

                # dotarcie do ujścia
                if u == t:
                    return (C_res[t], parent)

                Q.append(u)

    return (0, None)


def maxFlow(C, s, t):
    n = len(C)
    fmax = 0  # max przepływ

    C_res = [float('inf')] * n  # przepustowość sieci rezydualnej
    F = [[0 for _ in range(n)] for _ in range(n)]  # aktualny przepływ w sieci

    while True:
        # bfs szuka którędy jeszcze można puścić przepływ
        flow, parents = bfs(C, F, C_res, s, t)

        # przepływ == 0 oznacza, że osiągneliśmy max przepływ
        if flow == 0:
            break

        # zwiększamy przepływ o nową ścieżkę
        fmax += flow

        # idąc od końca po parentach aktualizujemy listę z przepływem
        v = t
        while v != s:
            p = parents[v]
            F[p][v] += flow
            F[v][p] -= flow
            v = p

    print(fmax)


s = 0
t = 6

#    s  A  B  C  D  E  t
C = [
    [0, 9, 0, 0, 9, 0, 0],  # s
    [0, 0, 7, 3, 0, 0, 0],  # A
    [0, 0, 0, 4, 0, 0, 6],  # B
    [0, 0, 0, 0, 0, 2, 9],  # C
    [0, 0, 0, 3, 0, 6, 0],  # D
    [0, 0, 0, 0, 0, 0, 8],  # E
    [0, 0, 0, 0, 0, 0, 0],  # t
]

maxFlow(C, s, t)
