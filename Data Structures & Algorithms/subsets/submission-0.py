class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]
        def helper(i, tempArray):
   
            tempArray.append(nums[i])
            output.append(tempArray.copy())
            for j in range(i+1, len(nums)):
                helper(j, tempArray)
            tempArray.remove(nums[i])

        
   
        for i in range(0,len(nums)):
            temp = []
            helper(i, temp)
        
        return output


