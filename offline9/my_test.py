from collections import deque


def bfs(C, F, C_res, s, t):
    n = len(C)
    parent = [-1] * n  # parenty
    Q = deque()

    Q.append(s)
    parent[s] = -2

    while Q:
        v = Q.popleft()

        for u in range(n):
            res_capacity = C[v][u] - F[v][u]

            if res_capacity > 0 and parent[u] == -1:
                parent[u] = v
                C_res[u] = min(res_capacity, C_res[v])

                if u == t:
                    return (C_res[t], parent)

                Q.append(u)
    return (0, None)


def maxFlowToVertex(C, s, t):
    n = len(C)
    fmax = 0

    C_res = [float('inf')] * n
    F = [[0 for _ in range(n)] for _ in range(n)]

    while True:
        flow, parents = bfs(C, F, C_res, s, t)

        if flow == 0:
            return fmax

        fmax += flow

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
    for start, end, flow in G:
        C[start][end] = flow

    fmax = 0
    start_flow_sum = sum(C[s])  # suma tego co wyplywa z wierzcholka

    a = 0
    b = 0

    # superwierzchołek, czyli sąsiad źródła - cokolwiek
    for v in range(n - 1):
        if v != s:
            for u in range(v+1, n - 1):
                if u != s:
                    print(v, u)
                    C[v][t] = float('inf')
                    C[u][t] = float('inf')
                    flow = maxFlowToVertex(C, s, t)
                    # print(flow)

                    if flow == start_flow_sum:
                        #print(v, u)
                        return flow

                    if flow > fmax:
                        a = v
                        b = u
                        fmax = flow

                    C[v][t] = 0
                    C[u][t] = 0
    print(a, b)
    return fmax


G = [(0, 1, 10), (0, 2, 15), (0, 5, 7), (0, 6, 10), (1, 3, 11),
     (2, 3, 18), (3, 4, 5), (5, 6, 15), (6, 7, 12)]
print(maxflow(G, 0))
