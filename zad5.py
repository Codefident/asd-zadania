# Piotr Klęp

# ====================== ZŁOŻONOŚĆ CZASOWA ======================

# O(mlogm + nlogk))

# ...ponieważ sortowanie + n-razy put() lub get() w PriorityQueue

# gdzie:
# k - ilość plam oleju
# m - ilość postojów

# ======================== ROZWIĄZANIE ========================

# Poruszamy się po tablicy T do momentu, gdy w cysternie
# skończy się paliwo, cały czas dodając do kolejki priorytetowej
# kolejne plamy oleju.

# Gdy paliwo się skończy, zasysamy ropę z największej plamy
# jaką dotychczas spotkaliśmy i jedziemy dalej.

# Innymi słowy - koniec paliwa oznacza że musimy się
# wcześniej zatankować. Plamy możemy brać w różnej kolejności,
# chodzi tylko o ich wielkość i o to czy są przed nami czy nie.
# Stąd konieczność posortowania listy wynikowej.

# =================== POPRAWNOŚĆ ALGORYTMU ===================


from zad5testy import runtests
from queue import PriorityQueue


def plan(T):
    n = len(T)

    oil = PriorityQueue() # plamy oleju
    stops = [0] # przystanki
    to_go = T[0] # ile jeszcze możemy przejechać

    for i in range(1, n-1):
        to_go -= 1

        if T[i] > 0:
            oil.put(( -T[i] , i )) # "-" ze względu na priorytet dla największego T[i]

        if to_go == 0:
            (fc, fi) = oil.get()
            fc *= -1
            to_go = fc
            stops.append(fi)

            if i + to_go >= n - 1:
                break

    return sorted(stops)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( plan, all_tests = True )