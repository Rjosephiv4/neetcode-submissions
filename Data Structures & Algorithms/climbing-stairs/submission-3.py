class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 1 or n == 0:
            return 1
        
        vals = [1,1]
        i = 2

        while i < n:
            temp = vals[1]
            vals[1] = vals[1] + vals[0]
            vals[0] = temp
            i+=1
        return vals[0] + vals[1]