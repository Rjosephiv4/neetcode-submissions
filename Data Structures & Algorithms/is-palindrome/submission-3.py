class Solution:
    def isPalindrome(self, s: str) -> bool:

        newWord = ""
        
        for letter in s:
            if letter.isalnum():
                newWord += letter.lower()
        
        print(newWord)
        n = len(newWord)
        n1 = 0
        n2 = n - 1 
        while n2 >= n1:
            if(newWord[n1] != newWord[n2]):
                return False
            n1+=1
            n2-=1
        return True