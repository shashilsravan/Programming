# def rotateImage(matrix: list):
#     if len(matrix[0]) == 0 or len(matrix[0][0]) == 0:
#         return
#     n = len(matrix[0])
#
#     for i in range(n//2 + n % 2):
#         for j in range(n//2):
#             temp = matrix[n - 1 - j][i]
#             matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
#             matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
#             matrix[j][n - 1 - i] = matrix[i][j]
#             matrix[i][j] = temp


# def rotateImage(matrix):
#     n = len(matrix[0])
#     for i in range(n):
#         for j in range(i+1, n):
#             matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
#     for i in range(n):
#         matrix[i].reverse()
#     return matrix


import numpy


def rotateImage(matrix: list):
    matrix = numpy.array(matrix)
    matrix = numpy.transpose(matrix).tolist()
    for i in range(len(matrix)):
        matrix[i].reverse()

    return matrix


print(rotateImage([[1,2,3],[4,5,6],[7,8,9]]))