class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums)==1:
            return nums[0]
        sub_array1 = nums[1:]
        sub_array2 = nums[0:len(nums)-1]
        

        def findSum(array):
            if len(array)<1:
                return 0
            if len(array) < 2:
                return array[0]

            first = array[0]
            second = max(array[0],array[1])
            i=2

            while i < len(array):
                third = max(first + array[i], second)
                first = second
                second = third
                i+=1
            
            return second
        
        return max(findSum(sub_array1), findSum(sub_array2))