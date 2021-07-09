def hammingDistance(x, y):
    x = x ^ y
    total = 0
    while x:
        total += 1
        x = x & (x-1)
    return total

print(hammingDistance(1, 4))