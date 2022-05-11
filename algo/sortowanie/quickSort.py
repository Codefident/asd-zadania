T = [5, 4, 1, 2, 8, 7, 6, 3, 9]


def partition(T, p, r):
    x = T[r]
    i = p - 1

    for j in range(p, r):
        if T[j] <= x: # to co jest mniejsze od x chcemy mieć przed x
            i += 1 # w indeks [i] wkładamy te mniejszą wartość
            T[i], T[j] = T[j], T[i]

    T[i+1], T[r] = T[r], T[i+1] # w środek wkładamy x
    return i + 1


def quickSort(T, p, r):
    while p < r:
        q = partition(T, p, r)
        quickSort(T, p, q-1)
        p = q + 1


quickSort(T, 0, len(T)-1)
print(T)