from zad1ktesty import runtests


def roznica(S: str):

    n = len(S)
    i = 0

    for char in S:
        if char == '0':
            break
        i += 1

    if i == n:
        return -1

    max_diff = 0
    diff = 0

    while i < n:

        if diff < 0 and S[i] == '1':
            for _ in range(i, n):
                i += 1
                if S[i] == '0':
                    break

        elif S[i] == '0':
            if diff < 0:
                diff = 0  # liczymy od nowa od nowego 0
            diff += 1
            i += 1

        else:
            if diff > max_diff:
                max_diff = diff
            diff -= 1
            i += 1

    return max_diff


runtests(roznica)
