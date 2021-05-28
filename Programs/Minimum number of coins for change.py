def coinChange(coins, amount):
    ways = [float("inf")] * (amount + 1)
    ways[0] = 0
    for each in coins:
        for i in range(1, len(ways)):
            if each <= i:
                ways[i] = min(ways[i], 1 + ways[i - each])
    return ways[amount] if ways[amount] != float("inf") else -1


print(coinChange([1, 2, 5], 11))