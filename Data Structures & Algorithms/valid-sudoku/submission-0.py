class Solution(object):
    def isValidSudoku(self, board):
        # 9 x 9 Board
        # each row has 1-9 without duplicates
        # each column has 1-9 without duplicates
        # each of the nine 3x3 boxes do not contain duplicates 

        rows = {}
        columns = {}
        squares = {}

        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                k = -1

                if i < 3:
                    if j < 3:
                        k = 0
                    elif j >= 6:
                        k = 2
                    else:
                        k = 1
                elif i >= 6:
                    if j < 3:
                        k = 6
                    elif j >= 6:
                        k = 8
                    else:
                        k = 7
                else:
                    if j < 3:
                        k = 3
                    elif j >= 6:
                        k = 5
                    else:
                        k = 4

                if i not in rows:
                    rows[i] = {}

                if j not in columns:
                    columns[j] = {}

                if k not in squares:
                    squares[k] = {}

                if board[i][j] != "." and (
                    board[i][j] in rows[i] or
                    board[i][j] in columns[j] or
                    board[i][j] in squares[k]
                ):
                    return False

                if board[i][j] != ".":
                    rows[i][board[i][j]] = True
                    columns[j][board[i][j]] = True
                    squares[k][board[i][j]] = True

        return True