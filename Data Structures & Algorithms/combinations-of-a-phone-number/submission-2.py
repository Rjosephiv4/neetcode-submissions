class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits =="":
            return []
        letter = ord("a")
        store = {}
        for i in range(2, 10):
            if i != 7 and  i !=9:
                for j in range(0,3):
                    array = store.get(i, [])
                    array.append(chr(letter))
                    store[i] = array
                    letter+=1
            else:
                for j in range(0,4):
                    array = store.get(i, [])
                    array.append(chr(letter))
                    store[i] = array
                    letter+=1

        string = []
        output = []
        def helper(i):
            if i >= len(digits):
                output.append("".join(string))
                return
            for letter in store[int(digits[i])]:
                string.append(letter)
                helper(i+1)
                string.pop()

        helper(0)
        return output
