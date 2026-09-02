class Solution:
    def minWindow(self, s: str, t: str) -> str:
        frq2 = {}

        for letter in t:
            frq2[letter] = frq2.get(letter, 0) + 1
        

        frq1 = {}
        string = ""
        answer = ""
        matches = 0
        matchLength =  float('inf')

        
        l = 0
        r = 0

        while r < len(s):
            char_r = s[r]
            frq1[char_r] = frq1.get(char_r, 0) + 1
            if char_r in frq2 and frq1[char_r] == frq2[char_r]:
                matches += 1
            
            while matches == len(frq2):
                current_len = r - l + 1
                if current_len < matchLength:
                    matchLength = current_len
                    answer = s[l:r+1]
                
                char_l = s[l]
                if char_l in frq2 and frq1[char_l] == frq2[char_l]:
                    matches -= 1
                frq1[char_l] -= 1
                l += 1
            r += 1
            
        return answer