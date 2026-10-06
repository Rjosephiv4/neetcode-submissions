class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[-1 for _ in range(0, n)] for i in range(0, m)] 
        for i in range(0, m-1):
            memo[i][n-1] = 1
        for j in range(0, n-1):
            memo[m-1][j] = 1
        

        def helper(i,j):
            if i == m-1 and j == n-1:
                return 1
            if i == m-1:
                return 1
            if j == n:
                return 1
            if memo[i][j] != -1:
                return memo[i][j]
            
            result = helper(i+1, j) + helper(i, j+1)
            memo[i][j] = result

            return result
        return helper(0,0)
            


