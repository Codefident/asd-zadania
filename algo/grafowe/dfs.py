def DFS(G):
    n = len(G)
    visited = [False] * n
    parents = [None] * n
    time = 0

    for v in range(n):
        if not visited[v]:
            DFSVisit(G, v)

    def DFSVisit(G: list, v: int):
        nonlocal time
        time += 1
        for u in G[v]:
            if not visited[u]:
                parents[u] = v
                DFSVisit(G, u)