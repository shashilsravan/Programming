def reverse(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start, end = start + 1, end - 1
    return nums


def rotate(nums, k):
    n = len(nums)
    k %= n
    nums = reverse(nums, 0, n - 1)
    nums = reverse(nums, 0, k - 1)
    nums = reverse(nums, k, n - 1)
    return nums

n = int(input())
nums = [int(x) for x in input().split()]
k = int(input())
print(rotate(nums, k))