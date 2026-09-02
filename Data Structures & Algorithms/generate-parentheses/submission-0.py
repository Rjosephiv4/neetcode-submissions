class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []

        l = 0
        r = 0

        def traverse(curr,l,r):
            if l == n:
                while r!= n:
                    curr+=")"
                    r+=1
                output.append(curr)
            

            if l < n:

                traverse(curr + "(",l+1,r)
            if r < l:
                traverse(curr+ ")",l,r+1)
        
        traverse("",0,0)
        return output