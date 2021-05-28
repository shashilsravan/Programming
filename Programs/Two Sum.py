# Two number sum problem
# finding two numbers in an array that sums up target element

arr = [5, 21, 12, -2, 15, 2, 9, -5]
target_sum = 10

# O(N)
# def two_sum(array: list, target: int):
#     nums = {}
#     for num in array:
#         match = target - num
#         if match in nums:
#             return [num, match]
#         else:
#             nums[num] = True
#     return []


# O(n logN)
def two_sum(array: list, target: int):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        current_sum = array[left] + array[right]
        if current_sum == target:
            return [array[left], array[right]]
        elif current_sum < target:
            left += 1
        elif current_sum > target:
            right -= 1
    return []


print(two_sum([5, 8, 12, 13, 17, 20, 22, 25], 37))