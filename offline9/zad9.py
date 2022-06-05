from collections import deque
from zad9testy import runtests


def maxFlowToVertex(C, s, t):
    n = len(C)
    fmax = 0

    P = [-1] * n  # poprzedniki
    C_res = [None] * n  # pojemność dla sieci rezydualnej
    F = [[0 for _ in range(n)] for _ in range(n)] # przepływ
    Q = deque()

    while True:
        for i in range(n):
            P[i] = -1

        P[s] = -2
        C_res[s] = float('inf')
        Q.clear()
        Q.append(s)
        escape = False

        while Q:
            v = Q.popleft()

            for u in range(n):
                res_capacity = C[v][u] - F[v][u]

                if res_capacity != 0 and P[u] == -1:
                    P[u] = v
                    C_res[u] = min(res_capacity, C_res[v])

                    # ścieżka kompletna jeśli...
                    if u == t:
                        fmax += C_res[t]

                        i = u
                        while i != s:
                            x = P[i]
                            F[x][i] += C_res[t]
                            F[i][x] -= C_res[t]
                            i = x
                        escape = True
                        break
                    Q.append(u)
            if escape:
                break
        if not escape:
            break
    return fmax


def maxflow(G, s):
    # +2 ponieważ +1 (źródło) +1 (tzw. superwierzchołek)
    n = max(G, key=lambda z: z[1])[1] + 2
    t = n - 1

    C = [[0] * n for _ in range(n)]  # pojemnosci

    for start, end, flow in G:
        C[start][end] = flow

    F = [[0] * n for _ in range(n)]  # przeplywy

    max_flow = 0
    start_flow_sum = sum(C[s])  # suma tego co wyplywa z wierzcholka

    # superwierzchołek, czyli sąsiad źródła - cokolwiek
    for v in range(n - 1):
        if v != s:
            for u in range(v + 1, n - 1):
                if u != s:

                    C[v][t] = float('inf')
                    C[u][t] = float('inf')

                    flow = maxFlowToVertex(C, s, t)

                    if flow == start_flow_sum:
                        return flow

                    max_flow = max(max_flow, flow)

                    C[v][t] = 0
                    C[u][t] = 0

    return max_flow


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(maxflow, all_tests=True)
