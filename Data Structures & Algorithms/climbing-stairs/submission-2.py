class Solution:
    def climbStairs(self, n: int) -> int:

        def helper(n,cache):
            if cache.get(n,-1) != -1:
                return cache[n]
            if n == 0:
                return 1
            if n == 1:
                return 1
            
            else:
                result = helper(n-1,cache) + helper(n-2,cache)
                cache[n] = result
                return result

        return helper(n,{})