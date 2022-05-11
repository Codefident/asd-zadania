from collections import deque


class Vertex:
    def __init__(self, i):
        self.i = i   # number/index of vertex
        self.d = -1   # distance from vertex s
        self.parent = None   # parent vertex
        self.visited = False


def BFS(G, s, t):

    e = len(G)
    Q = deque()
    V = []

    for i in range(e):
        V.append(Vertex(i))

    V[s].d = 0
    V[s].visited = True
    Q.appendleft(s)

    while Q:
        u = Q.popleft()
        # sąsiedzi u, v to numer indeksu
        for v in G[u]:
            if not V[v].visited:
                V[v].visited = True
                V[v].d = V[u].d + 1
                V[v].parent = u
                Q.append(v)

    if V[t].visited:
        i = t
        while i != s:
            print(i, "<=", end=" ")
            i = V[i].parent
        print(i)
    else:
        print('brak sciezki')


# G = [
#     [1, 4],  # 0
#     [0, 2],  # 1
#     [1, 3],  # 2
#     [2, 5],  # 3
#     [0, 5],  # 4
#     [4, 3]]  # 5

G = [[1, 2],  # 0
      [0, 3],  # 1
      [0, 4],  # 2
      [1, 5, 6],  # 3
      [2, 7],  # 4
      [3, 8],  # 5
      [3, 8],  # 6
      [4, 8],  # 7
      [5, 6, 7, 9],  # 8
      [8, 10, 11],  # 9
      [9, 12],  # 10
      [9, 12],  # 11
      [10, 11]]  # 12

BFS(G, 0, 12)
