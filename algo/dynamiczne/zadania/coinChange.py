# coin change

coins = [1, 5, 8]
amount = 15


def changeCoins(coins, amount):
    memo = [amount + 1] * (amount + 1)
    memo[0] = 0

    for a in range(1, amount + 1):
        for c in coins:
            if c <= a:
                memo[a] = min(memo[a], 1 + memo[a - c])
    
    if memo[amount] != amount + 1:
        return memo[amount]
    return -1

print(changeCoins(coins, amount))