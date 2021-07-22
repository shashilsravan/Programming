def palindromePermutation(string):
    hashmap = {}
    for each in string:
        if each in hashmap:
            hashmap.pop(each)
        else:
            hashmap[each] = True
    return len(hashmap) < 2