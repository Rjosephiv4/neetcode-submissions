class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        inputs = {}
        for num in nums:
            if num in inputs:
                inputs[num] +=1
            else:
                inputs[num] =1
        total = 0

        for num in nums:
            if num == 0:
                continue
            else: 
                if total == 0:
                    total = 1 
                total *= num


        answer = []
        for num in nums:
            if 0 in inputs and ((inputs[0] == 1 and num != 0) or inputs[0] > 1):
                answer.append(0)
            elif 0 in inputs and (inputs[0] ==1 and num ==0):
                answer.append(int(total))
            else:
                answer.append( int(total/num))


        return answer