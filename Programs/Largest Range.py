# O(n) time complexity
# def largestRange(array):
#     longest = 0
#     bestRange = []
#     nums = {}
#     for num in array:
#         nums[num] = True
#     for num in array:
#         if not num in nums:
#             continue
#         nums[num] = False
#         currentLength = 1
#         left = num - 1
#         right = num + 1
#
#         while left in nums:
#             nums[left] = False
#             currentLength += 1
#             left -= 1
#
#         while right in nums:
#             nums[right] = False
#             currentLength += 1
#             right += 1
#
#         if currentLength > longest:
#             longest = currentLength
#             bestRange = [left + 1, right - 1]
#
#     # return bestRange
#     return longest

def largestRange(array):
    longest = 0
    nums_set = set(array)

    for num in array:
        if num - 1 not in nums_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in nums_set:
                current_num += 1
                current_streak += 1
            longest = max(longest, current_streak)
    return longest


print(largestRange([1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]))
print(largestRange([0,3,7,2,5,8,4,6,0,1]))