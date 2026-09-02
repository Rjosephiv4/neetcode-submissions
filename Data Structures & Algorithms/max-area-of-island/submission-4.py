class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i,j):
            if i >= len(grid) or j>=len(grid[0]) or i < 0 or j <0 or grid[i][j] == 0:
                return 0
            
            grid[i][j] = 0
            return dfs(i+1,j) + dfs(i-1,j) + dfs(i,j+1) + dfs(i,j-1) + 1

          

        maxCount = 0

        for i in range(0,len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] ==1:
                    count = dfs(i,j)
                    if count > maxCount:
                        maxCount = count
        
        return maxCount

