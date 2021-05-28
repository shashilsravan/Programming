# O(N)
# def isOutOfOrder(i, num, array):
#     if i == 0:
#         return num > array[i+1]
#     elif i == len(array) - 1:
#         return num < array[i-1]
#     return num > array[i+1] or num < array[i-1]
#
#
# def subArraySort(array):
#
#     if len(array) == 1:
#         return 0
#
#     minOutOfOrder = float("inf")
#     maxOutOfOrder = float("-inf")
#
#     for i, num in enumerate(array):
#         if isOutOfOrder(i, num, array):
#             minOutOfOrder = min(minOutOfOrder, num)
#             maxOutOfOrder = max(maxOutOfOrder, num)
#
#     if minOutOfOrder == float("inf"):
#         return 0
#
#     subarrayLeftIdx = 0
#     while minOutOfOrder >= array[subarrayLeftIdx]:
#         subarrayLeftIdx += 1
#
#     subarrayRightIdx = len(array) - 1
#     while maxOutOfOrder <= array[subarrayRightIdx]:
#         subarrayRightIdx -= 1
#
#     # return subarrayRightIdx - subarrayLeftIdx + 1
#     return [subarrayLeftIdx, subarrayRightIdx]

def subArraySort(array):
    left, right = 0, len(array)-1
    start, end = 0, -1
    maximum, minimum = float("-inf"), float("inf")

    while right >= 0:
        if array[left] >= maximum:
            maximum = array[left]
        else:
            end = left

        if array[right] <= minimum:
            minimum = array[right]
        else:
            start = right

        left += 1
        right -= 1
    return end - start + 1


print(subArraySort([2, 6, 4, 8, 10, 9, 15]))