def maxProfit(prices) -> int:
    minPrice = 1000000000
    maxProfit = 0
    for i in range(len(prices)):
        if prices[i] < minPrice:
            minPrice = prices[i]
        elif prices[i] - minPrice > maxProfit:
            maxProfit = prices[i] - minPrice
    return maxProfit

print(maxProfit([7,1,5,3,6,4]))