def maxSumIncreasingSequence(array):
    temp = [0 for _ in range(len(array))]

    for i in range(len(array)):
        temp[i] = array[i]

    for i in range(1, len(array)):
        for j in range(i):
            if array[i] > array[j] and temp[i] < temp[j] + array[i]:
                temp[i] = temp[j] + array[i]
                print(temp)

    return max(temp)
print(maxSumIncreasingSequence([8, 12, 2, 3, 15, 5, 7]))