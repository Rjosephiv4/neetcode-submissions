class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        memo = {}
        memo[len(nums)-1] = 1
        def helper(index):


            if index in memo:
                return memo[index]
            
            maxItem = 1
            for i in range(index+1, len(nums)):
                result = helper(i)
                if nums[i] > nums[index]:
                    result = 1 + helper(i)
                    maxItem = max(maxItem, result)
            
            
            memo[index] = maxItem

            return maxItem
        
        for i in range(0, len(nums)):
            helper(i)

        result = float("-inf")
        for _, val in memo.items():
            if val > result:
                result = val
        return result

        