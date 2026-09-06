class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) < 2:
            return nums[0]
        first = nums[0]
        second = max(nums[0],nums[1])
        i=2
        while i < len(nums):
            third = max(first + nums[i], second)
            first = second
            second = third
            i+=1
        
        return second