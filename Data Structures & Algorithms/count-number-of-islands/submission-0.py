class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0


        def kill(i,j):
            if grid[i][j] == "1":
                grid[i][j] = "0"
                if i + 1 < len(grid):
                    kill(i+1,j)
                if j +1 < len(grid[0]):
                    kill(i,j+1)
                if i - 1 >= 0:
                    kill(i-1,j)
                if j -1 >=0:
                    kill(i,j-1)

        for i in range(0, len(grid)):
            for j in range(len(grid[0])):

                if grid[i][j] == "1":
                    count+=1
                    kill(i,j)
        return count
        