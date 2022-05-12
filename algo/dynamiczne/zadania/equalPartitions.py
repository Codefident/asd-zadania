# equal partitions
# 2 partitions with same sums of elements

A = [1, 5, 11, 5]


def twoPartitions(A: list):
    suma = sum(A)
    n = len(A)
    half: int

    if suma % 2 == 0:
        half = suma // 2
    else:
        return None

    ans = []
    cache = [[0] * (half + 1)] * n

    for h in range(A[0], half + 1):
        cache[0][h] = A[0]

    for h in range(half + 1):
        for i in range(1, n):

            cache[i][h] = cache[i-1][h]

            if h - A[i] >= 0:
                cache[i][h] = max(
                    cache[i][h],
                    cache[i-1][h-A[i]] + A[i]
                )

    return ans if ans else None


twoPartitions(A)
