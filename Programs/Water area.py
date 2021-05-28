def waterArea(array):
    maximum = 0
    leftMax = [0] * len(array)
    for i in range(1, len(array)):
        maximum = max(maximum, array[i-1])
        leftMax[i] = maximum

    maximum = 0
    rightMax = [0] * len(array)
    for i in range(len(array)-2, -1, -1):
        maximum = max(maximum, array[i+1])
        rightMax[i] = maximum

    totalCapacity = 0
    finalMax = [0] * len(array)

    for i in range(len(array)):
        minHeight = min(leftMax[i], rightMax[i])
        if array[i] < minHeight:
            finalMax[i] = minHeight - array[i]
            totalCapacity += finalMax[i]
        else:
            finalMax[i] = 0
    print(totalCapacity)
    return finalMax


print(waterArea([0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]))