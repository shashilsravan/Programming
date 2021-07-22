def rob(nums):
    incl = 0
    excl = 0
    for each in nums:
        new_incl = max(incl, excl)
        incl = excl + each
        excl = new_incl
    return max(incl, excl)