class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = [] # []
        output = [0] *  len(temperatures) #[0,0,0]
        for index, item in enumerate(temperatures):
            while len(stack) > 0 and temperatures[stack[-1]] < item:
                index2 = stack.pop()
                output[index2] = index - index2
            stack.append(index)

        
        
        return output
        
            

            
        
