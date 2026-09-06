class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:



        # 0 1 2 3 

        index = len(cost)-2
        i = 0
        j = cost[len(cost)-1]


        while index > -1:
            minimum = cost[index] + min(i,j)
            i = j
            j = minimum
            index-=1
        
        return min(i,j)
