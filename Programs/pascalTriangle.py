def generate(numRows):
    triangles = []
    for i in range(numRows):
        row = [None for _ in range(i + 1)]
        row[0], row[-1] = 1, 1

        for j in range(1, len(row)-1):
            row[j] = triangles[i - 1][j] + triangles[i][j-1]
        triangles.append(row)
    return triangles