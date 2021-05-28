def isValidSudoku(board: list):
    row = {i: [] for i in range(9)}
    col = {i: [] for i in range(9)}
    box = {i: [] for i in range(9)}

    for r in range(9):
        for c in range(9):
            if board[r][c] != ".":
                # check if the number in row
                if board[r][c] in row[r]:
                    return False
                else:
                    row[r].append(board[r][c])

                # check if the number in col
                if board[r][c] in col[c]:
                    return False
                else:
                    col[c].append(board[r][c])

                # Check if number in box
                # formula for box
                b = (r // 3) * 3 + (c // 3)
                if board[r][c] in box[b]:
                    return False
                else:
                    box[b].append(board[r][c])
    print(row, col, box)

    return True


isValidSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."]
                  , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                  , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                  , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                  , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                  , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                  , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                  , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                  , [".", ".", ".", ".", "8", ".", ".", "7", "9"]])
