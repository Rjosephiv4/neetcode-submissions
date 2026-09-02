class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashSet = {}

        for letter in s:
            if letter not in hashSet:
                hashSet[letter] = 1
            else:
                hashSet[letter] +=1
        
        for letter in t:
            if letter not in hashSet:
                return False
            else:
                hashSet[letter] -=1
        
        for letter in hashSet:
            if hashSet[letter] != 0:
                return False
        return True
            