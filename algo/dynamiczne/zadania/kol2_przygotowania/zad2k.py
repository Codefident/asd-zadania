from zad2ktesty import runtests


def palindrom(S: str):
    ans = ""
    ans_n = 0
    n = len(S)

    for i in range(n):

        # odd number of chars, ex. 'aba'
        k, j = i, i
        while k >= 0 and j < n and S[k] == S[j]:
            if j - k + 1 > ans_n:
                ans_n = j - k + 1
                ans = S[k:j+1]
            k -= 1
            j += 1

        # even, ex. 'abba'
        k, j = i, i + 1
        while k >= 0 and j < n and S[k] == S[j]:
            if j - k + 1 > ans_n:
                ans_n = j - k + 1
                ans = S[k:j+1]
            k -= 1
            j += 1

    return ans


runtests(palindrom)
