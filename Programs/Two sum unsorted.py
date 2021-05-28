def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    hashtable = {}
    for i, num in enumerate(nums):
        potentialMatch = target - num
        if potentialMatch in hashtable:
            return [hashtable[potentialMatch], i]
        hashtable[num] = i
    return []

print(twoSum([3, 3], 6))