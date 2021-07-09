def hammingWeight(n):
    total = 0
    while n != 0:
        total += 1
        n = n & (n-1)
    return total

print(hammingWeight("00000000000000000000000000001011"))