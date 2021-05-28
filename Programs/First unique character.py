def firstUniqChar(s):
    hashset = {}
    for i, num in enumerate(s):
        if num in hashset:
            hashset[num] = -1
        else:
            hashset[num] = i
    for value in hashset.values():
        if value != -1:
            return value
    return -1