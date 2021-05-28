def change(amount, coins):
    ways = [0] * (amount + 1)
    ways[0] = 1

    for each in coins:
        for i in range(1, len(ways)):
            if each <= i:
                ways[i] += ways[i - each]
            else:
                continue
    return ways[amount]


print(change(5, [1, 2, 5]))