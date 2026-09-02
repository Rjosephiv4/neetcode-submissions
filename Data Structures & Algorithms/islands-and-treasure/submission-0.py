class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = collections.deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]== 0:
                    queue.appendleft((i,j))
        
        while len(queue) > 0:
            x, y = queue.pop()

            if x+1 < len(grid):
                if grid[x+1][y] == 2147483647:
                    grid[x+1][y] = grid[x][y] + 1
                    queue.appendleft((x+1,y))
            if y+1 < len(grid[0]):
                if grid[x][y+1] == 2147483647:
                    grid[x][y+1] = grid[x][y] + 1
                    queue.appendleft((x,y+1))
            if x-1 >= 0:
                if grid[x-1][y] == 2147483647:
                    grid[x-1][y] = grid[x][y] + 1
                    queue.appendleft((x-1,y))
            if y-1 >=0:
                if grid[x][y-1] == 2147483647:
                    grid[x][y-1] = grid[x][y] + 1
                    queue.appendleft((x,y-1))

                


            