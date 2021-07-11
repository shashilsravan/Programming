def threeSum(nums):
    if len(nums) < 3:
        return []
    nums.sort()
    result = set()
    for i in range(1, len(nums[:-2])):
        if i >= 1 and nums[i] == nums[i-1]:
            continue

        hashmap = {}
        for x in nums[i+1:]:
            if x not in hashmap:
                hashmap[-nums[i]-x] = True
            else:
                result.add((nums[i], -nums[i]-x, x))
    return map(list, result)