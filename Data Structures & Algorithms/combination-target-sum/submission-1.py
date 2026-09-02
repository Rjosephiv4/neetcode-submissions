class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        subset = []
        
        def dfs(i, current_sum):
            if i >= len(nums) or current_sum > target:
                return 
            if current_sum == target:

                output.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i, current_sum + nums[i])
            subset.remove(nums[i])
         
            if i + 1 < len(nums):
                dfs(i+1, current_sum)


        dfs(0,0)
        return output