# Piotr Klęp
#
# ===== ZŁOŻONOŚĆ =====
#
#   O(V^4)
#
#
# ===== OPIS =====
#
# Program działa w oparciu o metodę Forda-Folkersona.
# Przekształcam dostarczoną listę miast w graf
# o reprezentacji macierzowej.
#
# Dodaję do niego dodatkowy wierzchołek który będzie ujściem,
# Nazywam go "superwierzchołkiem", gdyż jego zadaniem jest
# połączyć oba miasta, w których przepływ jest rozwiązaniem zadania.
#
# Krocząc dwoma pętlami szukam algorytmem Edmondsa-Karpa dla jakiej
# pary wierzchołków otrzymujemy największy przepływ i zwracam go
# jako wynik.

from collections import deque
from zad9testy import runtests


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


def maxFlowToVertex(C, s, t):
    n = len(C)
    fmax = 0  # max przepływ

    C_res = [float('inf')] * n  # przepustowość sieci rezydualnej
    F = [[0 for _ in range(n)] for _ in range(n)]  # aktualny przepływ w sieci

    while True:
        # bfs szuka którędy jeszcze można puścić przepływ
        flow, parents = bfs(C, F, C_res, s, t)

        # przepływ == 0 oznacza, że osiągneliśmy max przepływ
        if flow == 0:
            return fmax

        # zwiększamy przepływ o nową ścieżkę
        fmax += flow

        # idąc od końca po parentach aktualizujemy listę z przepływem
        v = t
        while v != s:
            p = parents[v]
            F[p][v] += flow
            F[v][p] -= flow
            v = p


def maxflow(G, s):
    # +2 ponieważ +1 (źródło) +1 (tzw. superwierzchołek)
    n = max(G, key=lambda z: z[1])[1] + 2
    t = n - 1

    C = [[0] * n for _ in range(n)]  # pojemnosci

    # reprezentacja macierzowa
    for start, end, flow in G:
        C[start][end] = flow

    max_flow = 0
    start_flow_sum = sum(C[s])  # suma tego co wyplywa z wierzcholka

    for v in range(n - 1):
        if v != s:
            for u in range(v + 1, n - 1):
                if u != s:

                    # dodajemy tu superwierzchołek pomiędzy dwiema krawędziami
                    C[v][t] = float('inf')
                    C[u][t] = float('inf')

                    flow = maxFlowToVertex(C, s, t)

                    # przepływ do danego wierzchołka nie może być większy niż łączny przepływ ze źródła
                    if flow == start_flow_sum:
                        return flow

                    max_flow = max(max_flow, flow)

                    # ... a tutaj go usuwamy
                    C[v][t] = 0
                    C[u][t] = 0

    return max_flow


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(maxflow, all_tests=True)
