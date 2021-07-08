from collections import Counter
def romanToInt(s):
    romanHash = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I":1}
    total = 0
    previous = 0
    for each in s:
        current = romanHash[each]
        if current > previous:
            total += current - 2 * previous
        else:
            total += current
        previous = current
    return total

print(romanToInt("IV"))