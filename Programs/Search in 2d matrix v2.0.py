def searchMatrix(matrix, target):
    i = 0
    j = len(matrix[0]) - 1

    while i < len(matrix) and j > -1:
        if matrix[i][j] == target:
            return True
        elif target < matrix[i][j]:
            j -= 1
        else:
            i += 1
    return False