from zad9testy import runtests


def maxflow(G, s):
    # tu prosze wpisac wlasna implementacje
    max(G, key=lambda z: z[1]) + 1

    return 0


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(maxflow, all_tests=False)
