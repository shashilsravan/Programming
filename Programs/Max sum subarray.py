# Approach - 1
# def maxSubArray(nums):
#     for i in range(1, len(nums)):
#         if nums[i-1] > 0:
#             nums[i] += nums[i-1]
#     return max(nums)

# Approach - 2
def maxSubArray(nums):
    def daq(left, right):
        if left == right:
            return nums[left]
        middle = (left + right) // 2
        leftMax = daq(left, middle)
        rightMax = daq(middle+1, right)
        crossMax = crossmax(left, right, middle)
        return max(leftMax, rightMax, crossMax)

    def crossmax(left, right, middle):
        leftSum = 0
        leftMax = float("-inf")
        for i in range(middle, left-1, -1):
            leftSum += nums[i]
            leftMax = max(leftMax, leftSum)

        rightSum = 0
        rightMax = float("-inf")
        for i in range(middle+1, right+1):
            rightSum += nums[i]
            rightMax = max(rightSum, rightMax)
        return leftMax + rightMax

    return daq(0, len(nums) - 1)