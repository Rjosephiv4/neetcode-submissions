class Solution:
    def partition(self, s: str) -> List[List[str]]:
        output = []
        part = []
        def isPalindrome(s,i,j):
            length = j-i + 1
            if length == 1:
                return True
            if length <= 0:
                return False

            while i < j:
                if s[i] != s[j]:
                    return False
                i+=1
                j-=1
            return True
        
        def helper(i):
            if i >= len(s):
                output.append(part.copy())
                return
            for j in range(i, len(s)):
                if isPalindrome(s, i, j):
                    part.append(s[i:j+1])
                    helper(j+1)
                    part.pop()
            

    
        helper(0)
        return output
