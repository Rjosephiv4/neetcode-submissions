class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        index = 0
        current = float('-inf')
        maX = float('-inf')
        while index < len(nums):
            current = max(nums[index], nums[index]+ current)
            maX = max(current, maX)

            index+=1
        return maX