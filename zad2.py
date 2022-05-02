# Piotr Klęp

# ====================================================================================================================================

# Działanie algorytmu

# Sortuję quicksortem listę L rosnąco względem początków przedziałów.
# Następnie iteruję po posortowanej liście L "dzieląc ją" na podzbiory w których początki przedziałów są jednakowe.
# Z podzbiorów tych wyłaniam przedziały cechujące się największym rozmiarem (tj. największą wartością oznaczającą jego koniec).

# Równocześnie korzystam z zaimplementowanej samodzielnie struktury linked-listy, w której przechowuję kolejne największe przedziały.
# Rozumiem przez to największe przedziały ze wspomnianych wyżej podzbiorów. Jednakże warunkiem dołączenia takiego przedziału
# do linked listy jest fakt, aby poprzednio dodany przedział miał mniejszą wartość końca
# (tzn. przedział, który chcemy dodać, musi "sięgać wyżej". W przeciwnym razie dodawanie go do tej listy mija się z celem).

# Linked-lista ta przeznaczona jest do tego aby dla każdego zachowanego przedziału zliczać przedziały, które się w nim zawierają.
# On sam nie może zawierać się w żadnym innym przedziale, gdyż wynika to z faktu że jest największy w swoim podzbiorze,
# a każdy kolejny przedział zaczyna się "wyżej" niż on z racji posortowania listy L.

# Zwieńczeniem tegoż algorytmu jest wyciągnięcie największej wartości z linked-listy i zwrócenie jej
# (uprzednio zmniejszając o 1, wynika to ze specyfiki mojej implementacji).

# ====================================================================================================================================

# Złożoność obliczeniowa:
			
# (element algorytmu)	---	(złożoność)	---	(zł. pesymistyczna)
# ____________________________________________________________________________

# Sortowanie szybkie	---	O( n*log(n) )	---	O( n^2 )
# Przejście po liście	---	O( n*k )	---	O( n^2 )
# Szukanie maxa		---	O( k )		---	O( n )
# ____________________________________________________________________________

# ...gdzie k to ilość przedziałów, jakie znajdą się w linked-liście.

# ====================================================================================================================================


from zad2testy import runtests


class Node:
    def __init__(self, b):
        self.b = b # .b oznacza koniec przedziału
        self.c = 0 # licznik podprzedziałów
        self.next = None


def partition(L, p, r):
    x = L[r]
    i = p - 1
    for j in range(p, r):
        if L[j][0] <= x[0]:
            i += 1
            tmp = L[i]
            L[i] = L[j]
            L[j] = tmp
    tmp = L[i + 1]
    L[i + 1] = L[r]
    L[r] = tmp
    return i + 1


def quickSort(L, p, r):
    while p < r:
        q = partition(L, p, r)
        quickSort(L, p, q - 1)
        p = q + 1


def depth(L):

    max_r = 0
    n = len(L)

    quickSort(L, 0, n - 1)
    
    i = 0
    c = 0 # licznik
    h = Node(-1)
    f = h # od tego miejsca będziemy podnosić wartości h.c
    l = h # ostatni dodany element

    # przedzial - [a,b]
    while i < n:
        
        # takie same a
        c = 0
        j = i
        
        while j < n and L[j][0] == L[i][0]:

            c += 1
            e = f

            # zliczanie dla poprzednich
            while e != None:
                if L[j][1] <= e.b:
                    e.c += 1   
                e = e.next
            
            # wyznaczanie najwiekszego przedzialu z tym samym .a
            if L[j][1] > L[i][1]:
                i = j

            j += 1

        # jeżeli ostatni przedział ma .b mniejsze od i[1], powstaje nowy Node
        if L[i][1] > l.b:
            l.next = Node(L[i][1])
            l = l.next
            l.c = c

        # skip jeśli początki zakresów wykraczają poza .b
        while f.b <= L[i][0]:
            f = f.next

        i = j
            
    h = h.next

    while h != None:
        if h.c > max_r:
            max_r = h.c
        h = h.next
        
    return max_r - 1


runtests( depth ) 
