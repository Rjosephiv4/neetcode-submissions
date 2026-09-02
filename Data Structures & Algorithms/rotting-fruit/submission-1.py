class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.appendleft((i,j,0))
        
        maxVal = 0
        while q:
            i,j, l = q.pop()
            if l > maxVal:
                maxVal = l
            if i +1 < len(grid) and grid[i+1][j] == 1:
                grid[i+1][j]=2
                q.appendleft((i+1,j,l+1))
            if i - 1 >=0 and grid[i-1][j] == 1:
                grid[i-1][j]=2
                q.appendleft((i-1,j,l+1))
            if j + 1 < len(grid[0]) and grid[i][j+1] == 1:
                grid[i][j+1]=2
                q.appendleft((i,j+1,l+1))
            if j -1 >= 0 and grid[i][j-1] == 1:
                grid[i][j-1]=2
                q.appendleft((i,j-1,l+1))
            
        



        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1

        return maxVal
            



        