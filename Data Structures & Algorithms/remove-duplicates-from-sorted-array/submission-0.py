class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        previous = -999
        for i in range (0, len(nums)):
            if nums[i] != previous:
                previous = nums[i]
                nums[k] = previous
                k +=1
        return k