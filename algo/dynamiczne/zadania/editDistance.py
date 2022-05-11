# edit distance

# 2 words
# return minimum number of operations required to convert word 1 to word 2

# operations:
#   - insert character
#   - delete character
#   - replace character

# / | a | b | d | -
# a | 0 |   |   | 3
# c |   | 1 | 1 | 2
# d | 2 | 1 | 0 | 1
# - | 3 | 2 | 1 | 0

word1 = 'abdk'
word2 = 'acd'


def changeWords(w1: str, w2: str):
    n1 = len(w1)
    n2 = len(w2)

    T = [[float('inf') for j in range(n2 + 1)] for i in range(n1 + 1)]

    for i in range(n1 + 1):
        T[i][n2] = n1 - i
    for j in range(n2 + 1):
        T[n1][j] = n2 - j

    for i in range(n1 - 1, -1, -1):
        for j in range(n2 - 1, -1, -1):
            if w1[i] == w2[j]:
                T[i][j] = T[i+1][j+1]
            else:
                T[i][j] = 1 + min(T[i+1][j], T[i][j+1], T[i+1][j+1])

    return T[0][0]


print(changeWords(word1, word2))
