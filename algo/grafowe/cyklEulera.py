# cykl Eulera
# DFS bez visited, usuwając odwiedzone krawędzie
# gdy nie ma możliwości pójścia do innej krawędzi, to dopisujemy wierzchołek na początek listy


def eulerCycle(G: list):
    cycle = []
    parent = []
    
    return cycle


# 0 - brak krawędzi, 1 - istnieje krawędź
#    a, b, c, d, e, f
G = [
    [0, 1, 1, 0, 0, 0],  # a
    [1, 0, 1, 1, 0, 1],  # b
    [1, 1, 0, 1, 0, 1],  # c
    [0, 1, 1, 0, 1, 1],  # d
    [0, 0, 0, 1, 0, 1],  # e
    [0, 1, 1, 1, 1, 0]   # f
]
