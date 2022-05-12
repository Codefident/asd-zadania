from zad4ktesty import runtests


def falisz(T: list[list]):

    n = len(T)
    cache = [[0 for _ in range(n)] for _ in range(n)]

    cache[0][0] = T[0][0]

    for i in range(1, n):
        cache[0][i] += cache[0][i-1] + T[0][i]
        cache[i][0] += cache[i-1][0] + T[i][0]

    for i in range(1, n):
        for j in range(1, n):
            cache[i][j] = T[i][j] + min(cache[i-1][j], cache[i][j-1])

    if n <= 10:
        for row in cache:
            print(row)
    return cache[n-1][n-1]


runtests(falisz)
