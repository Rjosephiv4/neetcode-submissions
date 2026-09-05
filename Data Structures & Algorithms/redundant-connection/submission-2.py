class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        hashSet = {}

        for i in range(1,n+1):
            hashSet[i] = i
        
        for edge in edges:
            if hashSet[edge[0]] != hashSet[edge[1]]:
                old_val = hashSet[edge[1]]
                new_val = hashSet[edge[0]]
                for i in range(1, n+1):

                    if hashSet[i] == old_val:
                        hashSet[i] = new_val
            else:
                return edge
        
        return [-1,-1]