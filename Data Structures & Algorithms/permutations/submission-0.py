class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def traverse(i):
            if i == len(nums):
                return [[]]
            else:
                perms = traverse(i+1)
                
                output = []

                for element in perms:
                    for j in range(0, len(element)+1):
                        copy = element.copy()
                        copy.insert(j, nums[i])
                        output.append(copy)
                
                return output

        return traverse(0)

