class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0 
        right = len(nums) - 1
        

        while left < right:
            mid = math.floor((left + right)/2) # 5
            if nums[mid] > nums[right]: # 3 > 5
                left = mid+1
            else:
                right = mid
            
        return nums[left]

