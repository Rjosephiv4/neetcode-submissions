from collections import deque
class Solution:
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        leftPass = []
        rightPass = deque()
        product = 1
        for num in nums:
            product *= num
            leftPass.append(product)
        product = 1
        for i in range(len(nums)-1,-1, -1):
            product*= nums[i]
            rightPass.appendleft(product)
        
        output = []
        print(leftPass)
        print(rightPass)
        for i in range(0, len(nums)):
            left = 1
            right = 1
            if i - 1 >= 0:
                left = leftPass[i-1]
            if i+1 < len(nums):
                right = rightPass[i+1]
            
            output.append(left*right)
        return output
