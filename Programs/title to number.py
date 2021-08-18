def titleToNumber(columnTitle):
    columnTitle = columnTitle[::-1]
    total = 0
    for i in range(len(columnTitle)):
        total += ((ord(columnTitle[i]) - 65 + 1) * (26 ** i))
    return total


print(titleToNumber("FXSHRXW"))