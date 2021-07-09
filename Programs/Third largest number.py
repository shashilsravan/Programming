def storeInArray(arr, element):
    if arr[0] < element:
        arr = [element, arr[0], arr[1]]
    elif arr[1] < element:
        arr = [arr[0], element, arr[1]]
    elif arr[2] < element:
        arr = [arr[0], arr[1], element]
    return arr

def thirdMax(nums):
    nums = list(set(nums))
    if len(nums) < 3:
        return max(nums)
    arr = [float("-inf"), float("-inf"), float("-inf")]
    for each in nums:
        arr = storeInArray(arr, each)
    return arr[-1]

print(thirdMax([1, 2, 1]))