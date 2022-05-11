# longest common subsequence

# --- idea ---
# 2D array
#     3 _ 2 _ 3 _ 5 _ 7 _ 1 _ -
# 3 | x |                       |
# 4 |   | - | - | - | - | - |   |
# 2 |   | x |                   |
# 7 |   |   | - | - | x |       |
# 5 |       | - | x | - | - |   |
# 6 |               | - | - |   |
# 7 |               | x | - |   |
# 0 |                   | - |   |
# 1 |                   | x |   |
# 8 |                   | - |   |
# - |                       | 0 |

#     3 _ 2 _ 3 _ 5 _ 7 _ 1 _ -
# 3 | 5 |                     0 |
# 4 | 4 | - | - | - | - | - | 0 |
# 2 |   | 4 |                 0 |
# 7 |   |   | 3 | - | x |     0 |
# 5 |       | - | 3 | - | - | 0 |
# 6 |             2 | - | - | 0 |
# 7 |               | 2 | - | 0 |
# 0 |                 1 | - | 0 |
# 1 |                   | 1 | 0 |
# 8 |            max  b | 0 | 0 |
# - | 0 | 0 | 0 | a | b | 0 | 0 |

# a > b

# we go from the bottom

A = [3, 4, 2, 7, 5, 6, 7, 0, 1, 8]
B = [3, 2, 3, 5, 7, 1]

# output: 5


def lcs(A: list, B: list):
    T = [[0 for j in range(len(B) + 1)] for i in range(len(A) + 1)]

    for i in range(len(A) - 1, -1, -1):
        for j in range(len(B) - 1, -1, -1):
            if A[i] == B[j]:
                T[i][j] = T[i+1][j+1] + 1
            else:
                T[i][j] = max(T[i+1][j], T[i][j+1])

    return T[0][0]

print(lcs(A, B))
