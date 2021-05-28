def moveZeroes(nums):
    if len(nums) == 0 or len(nums) == 1:
        return nums
    left, right = 0, 0
    while right < len(nums):
        if nums[right] == 0:
            right += 1
        else:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right += 1
        print(nums)
    return nums


print(moveZeroes([4, 2, 0, 1, 3, 0, 3, 12, 0]))