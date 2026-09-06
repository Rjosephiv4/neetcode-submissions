class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        res = ""
        
        # Every single character is a palindrome
        for i in range(n):
            dp[i][i] = True
            res = s[i]
        
        # Check palindromes of length ≥ 2
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    # length 2 is special (no inner chars)
                    if length == 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                    
                    if dp[i][j] and length > len(res):
                        res = s[i:j + 1]
        
        return res