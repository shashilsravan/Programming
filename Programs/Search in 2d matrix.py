def searchMatrix(matrix, target):
    i = 0
    j = len(matrix[0])-1
    while i < len(matrix) and j >= 0:
        if matrix[i][j] == target:
            return True
        elif matrix[i][j] > target:
            j -= 1
        elif matrix[i][j] < target:
            i += 1
    return False

print(searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 22))

# [
# [1, 4, 7, 11,15],
# [2, 5, 8, 12,19],
# [3, 6, 9, 16,22],
# [10,13,14,17,24],
# [18,21,23,26,30]]