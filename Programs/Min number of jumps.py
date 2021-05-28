# def minJumps(nums):
#     dp = [float("inf") for _ in nums]
#     dp[0] = 0
#     for i in range(1, len(nums)):
#         for j in range(i):
#             if i <= nums[j] + j:
#                 dp[i] = min(dp[i], dp[j]+1)
#
#     return dp[-1]

def minJumps(array):
    if len(array) == 1:
        return 0
    jumps = 1
    maxReach = array[0]
    steps = array[0]
    for i in range(1, len(array) - 1):
        maxReach = max(maxReach, i + array[i])
        steps -= 1
        if steps == 0:
            jumps += 1
            steps = maxReach - i
    return jumps


print(minJumps([2, 3, 1, 1, 4]))