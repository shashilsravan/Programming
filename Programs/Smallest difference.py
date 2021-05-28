# Time complexity - O(n log(n) + m log(m))


def smallestDifference(arrayOne: list, arrayTwo: list):
    arrayOne.sort()
    arrayTwo.sort()
    idxOne = 0
    idxTwo = 0
    smallest = float("inf")
    current = float("inf")
    smallestPair = []

    while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
        firstNum = arrayOne[idxOne]
        secondNum = arrayTwo[idxTwo]
        current = abs(firstNum - secondNum)
        if firstNum < secondNum:
            idxOne += 1
        elif firstNum > secondNum:
            idxTwo += 1
        else:
            return [firstNum, secondNum]

        if smallest > current:
            smallest = current
            smallestPair = [firstNum, secondNum]

    return smallestPair


print(smallestDifference([-1, 5, 10, 20, 28, 3], [25, 134, 135, 15, 17]))