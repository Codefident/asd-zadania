T = [7, 6, 5, 3, 2, 9]


def left(i): return 2*i + 1
def right(i): return 2*i + 2
def parent(i): return (i - 1) // 2


def heapify(T, n, i):
    
    l = left(i)
    r = right(i)
    mi = i

    if l < n and T[l] > T[mi]:
        mi = l
    if r < n and T[r] > T[mi]:
        mi = r

    if mi != i:
        T[i], T[mi] = T[mi], T[i]
        heapify(T, n, mi)


def buildHeap(T, n):
    for i in range(parent(n - 1), -1, -1):
        heapify(T, n, i)


def heapSort(T):

    n = len(T)
    buildHeap(T, n)

    while n > 1:
        T[0], T[n-1] = T[n-1], T[0]
        n -= 1
        heapify(T, n, 0)


heapSort(T)
print(T)