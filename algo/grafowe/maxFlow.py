# problem maksymalnego przepływu
# algorymt Forda-Fulkersona / Edmondsa-Karpa (BFS)

from collections import deque


def maxFlow(C, s, t):
    n = len(C)
    fmax = 0

    P = [-1] * n  # poprzedniki
    CfP = [None] * n
    F = [[0 for _ in range(n)] for _ in range(n)]
    Q = deque()

    while True:
        for i in range(n):
            P[i] = -1

        P[s] = -2
        CfP[s] = float('inf')
        Q.clear()
        Q.append(s)
        escape = False

        while Q:
            v = Q.popleft()

            for u in range(n):
                residual_capacity = C[v][u] - F[v][u]

                if residual_capacity != 0 and P[u] == -1:
                    P[u] = v
                    CfP[u] = min(residual_capacity, CfP[v])

                    # ścieżka kompletna jeśli...
                    if u == t:
                        fmax += CfP[t]

                        i = u
                        while i != s:
                            x = P[i]
                            F[x][i] += CfP[t]
                            F[i][x] -= CfP[t]
                            i = x
                        escape = True
                        break
                    Q.append(u)
            if escape:
                break
        if not escape:
            break
    for x in range(n):
        for y in range(n):
            if C[x][y]:
                print(x, "->", y, ' ', F[x][y], ':', C[x][y])


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
