from collections import deque 
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()

        for token in tokens:

            if token == '+':
                x2 = stack.pop()
                x1 = stack.pop()
            

                stack.append(int(x1) + int(x2))
            elif token == '-':
                x2 = stack.pop()
                x1 = stack.pop()

                stack.append(int(x1) - int(x2))
            elif token == '*':
                x2 = stack.pop()
                x1 = stack.pop()

                stack.append(int(x1) * int(x2))
            elif token == '/':
                x2 = stack.pop()
                x1 = stack.pop()

                stack.append(int(float(x1)/float(x2)))
            else:
                stack.append(token)
        
        total = stack.pop()
        return int(total)
        
            