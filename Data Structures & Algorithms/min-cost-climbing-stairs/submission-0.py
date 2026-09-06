class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:


        def helper(i, cache):
            if i == len(cost) - 1 or i == len(cost) -2:
                cache[i] = cost[i]
                return cost[i]
            if i == len(cost):
                return 0
            
            if i in cache:
                return cache[i]

            
            else:
                result = cost[i] + min(helper(i+1, cache), helper(i+2, cache))
                cache[i] = result
                return result
        
        return min(helper(0,{}), helper(1,{}))