# Piotr Klęp

from asyncio import current_task
from zad4testy import runtests

def capacity(T, i):
    return T[i][0] * (T[i][2] - T[i][1])


def chooseMax(T, F, i, c):
    if F[i-1][c-T[i][3]][0] + T[i][0] > F[i][c][0]:
        return [ F[i-1][c-T[i][3]][0] + T[i][0], i ]
    return [ F[i][c][0] , F[i-1][c][1] ]


def collision(T, i, j):
    return T[i][1] > T[j][2]


def select_buildings(T,p):

    cpcty = 0
    a = 1
    b = 2
    cost = 3
    index = 4

    n = len(T)
    solution = []

    for i in range(n):
        T[i] = (capacity(T, i), T[i][a], T[i][b], T[i][cost], i)

    T = sorted(T, key = lambda building: building[2])

    # [capacity, last i-index]
    F = [[[-1, list()] for c in range(p + 1)] for i in range(n)]
    
    for c in range(T[0][cost], p + 1):
        F[0][c] = [ T[0][cpcty], [0] ]
    
    for c in range(p + 1):
        for i in range(1, n):

            F[i][c] = F[i-1][c].copy()

            if c - T[i][cost] >= 0:

                currCapacity = T[i][cpcty]
                currMax = F[i][c][0]
                currMax_j = -1

                for j in range(i-1, -1, -1):
                    if collision(T, i, j) and F[j][c-T[i][cost]][0] + currCapacity > currMax:
                        currMax = F[j][c-T[i][cost]][0] + currCapacity
                        currMax_j = j

                maxCapacity = max(F[i][c][0], currMax, currCapacity)

                if maxCapacity == currMax:
                    F[i][c] = F[currMax_j][c].copy()
                    F[i][c][1].append(i)
                
                elif maxCapacity == currCapacity:
                    F[i][c][1] = [i]
                
                F[i][c][cpcty] = maxCapacity


    for i in F[n-1][p][1]:
        solution.append(T[i][index])

    return solution

runtests( select_buildings )

