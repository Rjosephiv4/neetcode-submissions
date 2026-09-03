class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        def dfs(i,j):
            if i >= rows or j >=cols or i < 0 or j < 0 or board[i][j] != 'O':
                return
            
            board[i][j] = 'T'

            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)

        for i in range(rows):
            if board[i][cols-1] == "O":
                dfs(i,cols-1)
            if board[i][0] == "O":
                dfs(i,0)
        
        for i in range(cols):
            if board[0][i] == "O":
                dfs(0,i)
            if board[rows-1][i] == "O":
                dfs(rows-1,i)

            
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if board[i][j] == "T":
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"
