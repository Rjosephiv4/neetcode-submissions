class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #find the longest matching substring that has k extra characters

        l = 0
        letCount = {}
        letCount[s[0]] = 1
        maxf = 0
        result = 0
        for r in range(1, len(s)):
            if s[r] in letCount:
                letCount[s[r]] = letCount[s[r]] + 1
            else:
                letCount[s[r]] = 1

            maxf = max(maxf, letCount[s[r]])

            window_size = r-l + 1

            if window_size - maxf > k:
                letCount[s[l]] -= 1
                l = l+1
         

            result = max(result, r-l + 1)
                
        
        return result

