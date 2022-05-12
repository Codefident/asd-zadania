from zad3ktesty import runtests


def ksuma(T: list, k: int):
    n = len(T)

    if k == n:
        return min(T)
    if k == 1:
        return sum(T)

    sums = [float('inf')] * n + 1
    sums[0] = 0

    for i in range(1, n+1):
        pass



runtests(ksuma)
