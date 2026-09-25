class Solution:
    def numDecodings(self, s: str) -> int:
        table = {}
        def helper(i):
            if i == len(s):
                return 1
            if int(s[i]) == 0:
                return 0 
            if i in table:
                return table[i]

            if (int(s[i]) == 1 or int(s[i]) ==2) and i+1 < len(s):
                    if (int(s[i]) == 2 and int(s[i+1]) <= 6) or (int(s[i]) == 1):
                            result =  helper(i+1) + helper(i+2)
                            table[i] = result
                            return result
                    else:
                        result =  helper(i+1)
                        table[i] = result
                        return result
            result = helper(i+1)
            table[i]=result
            return result
        return helper(0)
                    