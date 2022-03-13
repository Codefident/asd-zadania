# name

from zad1testy import Node, runtests


def left(i): return 2 * i + 1
def right(i): return 2 * i + 2
def parent(i): return (i - 1) // 2


def heapify(A, n, i):
    l = left(i)
    r = right(i)
    min_i = i

    if l < n and A[l].val < A[min_i].val:
        min_i = l
    if r < n and A[r].val < A[min_i].val:
        min_i = r

    if min_i != i:
        tmp = A[i]
        A[i] = A[min_i]
        A[min_i] = tmp
        heapify(A, n, min_i)


def buildHeap(A, n):
    for i in range(parent(n - 1), -1, -1):
        heapify(A, n, i)


# zwraca wierzchołek (czyli minimum) z kopca i zastępuje go ostatnim elementem
# i naprawiając kopiec
def heapPop(A, n):
    res = A[0]
    A[0] = A[n - 1]
    heapify(A, n - 1, 0)
    return res


def heapSort(p, k):

    item = p

    # A - tablica na k+1 pierwszych wskaźników
    # A = [None for _ in range(k + 1)]
    # i = 0
    # while i < k + 1 and item != None:
    #     A[i] = item
    #     item = item.next # item wskazuje na pierszy element następujący zaraz po ostatnim z listy A
    #     i += 1
    # k = i
    
    A = []
    i = 0
    while i < k + 1 and item != None:
        A.append(item)
        item = item.next # item wskazuje na pierszy element następujący zaraz po ostatnim z listy A
        i += 1
    k = len(A)

    buildHeap(A, k)

    # początek posortowanej listy
    p = A[0]
    prev_item = p

    # wpięcie kolejnych minimum do listy i wrzucanie do tablicy A kolejnych Node'ów
    while item != None:
        A[0] = item
        heapify(A, k, 0)
        prev_item.next = A[0]
        prev_item = prev_item.next
        item = item.next

    # gdy skończą się Node'y zmniejszamy n czyli rozmiar kopca
    while k > 1:
        heapify(A, k, 0)

        # tym razem zdejmujemy za pomocą funkcji heapPop
        # ponieważ będziemy przestawiać Node'y wewnątrz kopca
        # bez doklejania nowych
        prev_item.next = heapPop(A, k)
        prev_item = prev_item.next
        k -= 1
    
    # dodanie do listy ostatniego elementu i zakończenie jej None'm
    prev_item.next = A[0]
    prev_item.next.next = None
    return p


def bubbleSort(p):
    a = p
    prev_a = p

    # początek posortowanej listy
    if a.val > a.next.val:
        p = a.next
        a.next = p.next
        p.next = a
        prev_a = a
        a = a.next
    
    while a != None and a.next != None:
        if a.val > a.next.val:
            prev_a.next = a.next
            prev_a = a.next
            a.next = prev_a.next
            prev_a.next = a

        prev_a = a
        a = a.next
 
    return p


def SortH(p,k):

    # O(1)
    if k == 0:
        return p

    # O(n)
    if k == 1:
        return bubbleSort(p)

    return heapSort(p, k)
        
    return p
    pass

runtests( SortH ) 
