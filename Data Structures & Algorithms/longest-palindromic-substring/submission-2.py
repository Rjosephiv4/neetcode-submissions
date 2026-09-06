class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        dp = [[False for i in range(len(s))] for i in range(len(s))]

        res = ""
        
        for i in range(0,n):
            dp[i][i] = True
            res=s[i]

        for length in range(2, n+1):
            for i in range(n-length+1):
                j = i + length -1

                if s[i] == s[j]:
                    if length == 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                    
                    if dp[i][j] and length > len(res):
                        res = s[i:j+1]
        
        return res