class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        biggest = 1
        seen = set()
        if len(s) < 1:
            return 0
        seen.add(s[0])
        for r in range(1, len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            
            if (r+1 - l) > biggest:
                biggest = r+1-l
            
            seen.add(s[r])
        return biggest