# choin change combination

# in how many ways we can give a change

coins = [1, 2, 5]
amount = 5


def takeCoin(i, a, coins):
    if i < 0:
        return 0

    a -= coins[i]

    if a < 0:
        return 0

    if a == 0:
        return 1

    return takeCoin(i, a, coins) + takeCoin(i - 1, a, coins)


def coinChangesOptions(coins, amount):
    combinations = 0

    for i in range(len(coins) - 1, -1, -1):
        combinations += takeCoin(i, amount, coins)

    print(combinations)


coinChangesOptions(coins, amount)