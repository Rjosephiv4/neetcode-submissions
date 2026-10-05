class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        memo = {}
        
        def helper(index):
            if index == len(s):
                return True
            
            if index in memo:
                return memo[index]            
            
            for i in range(len(s)):
                if s[index:index+i+1] in wordDict and helper(index+i+1):
                    memo[index] = True
                    return True
            memo[index] = False
            return False
        return helper(0)