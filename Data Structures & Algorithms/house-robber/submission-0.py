class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
        def helper(i,cache):
            if i in cache:
                return cache[i]
            
            if i >= len(nums):
                return 0

            value =  max(helper(i+2, cache), helper(i+3,cache))
            cache[i] = value +nums[i]
            return value + nums[i]
        
        return max(helper(0, {len(nums)-1:nums[len(nums)-1],len(nums)-2:nums[len(nums)-2]}),helper(1, {len(nums)-1:nums[len(nums)-1],len(nums)-2:nums[len(nums)-2]}) )