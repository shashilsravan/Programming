def maxSubsetSumNoAdjacent(arr):
    if len(arr) == 0 or not len(arr):
        return
    elif len(arr) == 1:
        return arr[0]

    incl = 0
    excl = 0

    for each in arr:
        curr_excl = max(incl, excl)
        incl = excl + each
        excl = curr_excl
    return max(incl, excl)


print(maxSubsetSumNoAdjacent([7, 10, 12, 7, 9, 14]))
