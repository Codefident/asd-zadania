T = [5, 4, 1, 2, 8, 7, 6, 3, 9]


def merge(T, p, q, r):
    i = p
    j = q + 1

    while i <= q:
        if T[i] > T[j]:
            T[i], T[j] = T[j], T[i]
            i += 1


def mergeSort(T, p, r):
    if p < r:
        q = p + ((r - p) // 2)
        mergeSort(T, p, q)
        mergeSort(T, q + 1, r)



mergeSort(T, 0, len(T)-1)
print(T)