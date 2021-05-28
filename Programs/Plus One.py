def plusOne(digits):
    for i in range(len(digits)-1, -1, -1):
        if digits[i] != 9:
            digits[i] += 1
            break
        else:
            digits[i] = 0

    if digits[0] == 0:
        digits.insert(0, 1)
    return digits


# print(plusOne([1, 2, 3, 4]))
print(plusOne([1, 2, 9, 9]))
print(plusOne([9, 9]))