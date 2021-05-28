# Time complexity: 0(N)
# def breaksDirection(direction, num1, num2):
#     difference = num2 - num1
#     if direction > 0:
#         return difference < 0
#     return difference > 0
#
#
# def isMonotonic(array):
#     if len(array) <= 2:
#         return True
#
#     direction = array[1] - array[0]
#
#     for i in range(2, len(array)):
#         if direction == 0:
#             direction = array[i] - array[i-1]
#             continue
#         if breaksDirection(direction, array[i-1], array[i]):
#             return False
#     return True


# Time complexity: O(N)
def isMonotonic(array):
    isIncreasing = True
    isDecreasing = True

    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            isIncreasing = False
        elif array[i] > array[i - 1]:
            isDecreasing = False
    return isIncreasing or isDecreasing


print(isMonotonic([1, 1, 2, 2, 2]))
