def findZeroes(num):
    res = 0
    while num >= 5:
        num = num // 5
        res += num
    return res


print(findZeroes(100))