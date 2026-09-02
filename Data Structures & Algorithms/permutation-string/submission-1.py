class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        counts1 = {}
        counts2 = {}
        total = len(s1)
        for l in s1:
            if l in counts1:
                counts1[l] += 1
            else:
                counts1[l] = 1
        
        for i in range(0, total):
            if s2[i] in counts2:
                counts2[s2[i]] += 1
            else:
                counts2[s2[i]] = 1
        
        l=0
        r = len(s1) - 1
        while r < len(s2):
            
            runner = 0
            for letter, count in counts1.items():
                if letter not in counts2 or counts2[letter] != count:
                    break
                
                runner += 1
                if runner == len(counts1):
                    return True
            
            counts2[s2[l]] -=1
            l+=1
            r+=1
            if r < len(s2):
                if s2[r] in counts2:
                    counts2[s2[r]]+=1
                else:
                    counts2[s2[r]] = 1

        return False
            
            
        

