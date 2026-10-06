class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        goal = sum(nums)
                
        if goal % 2 == 1:
            return False
        goal /= 2
        goal = int(goal)
        memo = {}
        def helper(target, i):
            if (i,target) in memo:
                return memo[(i,target)]
            if nums[i] == target:
                memo[(i,target)] = True
                return True
            for j in range(i+1, len(nums)):
                if helper(target - nums[i],j):
                    memo[(i,target)] = True
                    return True
            
            memo[(i,target)] = False
            return False

        return helper(goal,0)