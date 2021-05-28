def maxProfits(array):
    profit = 0
    for i in range(1, len(array)):
        profit += max(array[i] - array[i-1], 0)
    return profit


print(maxProfits([1, 1, 2, 5, 3, 4, 6, 1]))