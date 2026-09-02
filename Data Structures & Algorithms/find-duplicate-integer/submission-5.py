class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = 0
        slow = 0
        while fast != slow or fast == 0:
            fast = nums[nums[fast]]
            slow = nums[slow]
        
        slow = 0

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return fast