def productSum(arr, multiplier = 1):
    total = 0
    for element in arr:
        if type(element) is list:
            total += productSum(element, multiplier+1)
        else:
            total += element
    return total * multiplier

print(productSum([5, 2, [7, -1], 3, [6, [-13, 8], 4]]))