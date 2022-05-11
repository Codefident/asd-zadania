# cutting trees

# cutting a tree = different profit
# we want the highest profit
# but we cannot cut neighbouring trees

# f(n) = max( f(n-1), f(n) + f(n-2) )

trees = [5, 2, 1, 7, 3, 7, 3]
# output should be [0, 3, 5]


def cut(trees: list, i: int, T: list[(int, list)]):
    if i < 0:
        return (0, [])
    if T[i] != None:
        return T[i]

    v1 = cut(trees, i-2, T)
    v1 = (v1[0] + trees[i], v1[1])

    v2 = cut(trees, i-1, T)

    if v1 > v2:
        T[i] = (v1[0], v1[1].copy())
        T[i][1].append(i)
    else:
        T[i] = (v2[0], v2[1].copy())

    return T[i]


def cutTrees(trees):
    n = len(trees)
    T = [None] * n

    print(cut(trees, n-1, T))


cutTrees(trees)
