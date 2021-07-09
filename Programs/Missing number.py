def missingNumber(nums):
    n = len(nums)
    expectedSum = (n * (n + 1)) // 2
    actualSUm = sum(nums)
    return expectedSum - actualSUm