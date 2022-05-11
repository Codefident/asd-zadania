A = [2, 3, 7, 50, 0, 1000, 990]


def maxAltSubSum(A):
    sum = 0
    positive = True
    n = len(A)

    for i in range(n):

        # number is larger than (sum - number)
        if A[i] > sum and not positive:
            sum = A[i]
            positive = False

        # smallest number, -
        elif not positive:
            if (i + 1 < n and A[i + 1] < A[i]) or i + 1 >= n:
                continue
            else:
                sum -= A[i]
                positive = True

        # greatest number, +
        elif positive:
            if i + 1 < n and A[i + 1] > A[i]:
                continue
            else:
                sum += A[i]
                positive = False

    print(sum)
    return sum


maxAltSubSum(A)
