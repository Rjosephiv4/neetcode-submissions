class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        visiting = set()

        adjacency = collections.defaultdict(list)
        for edge in edges:
            adjacency[edge[0]].append(edge[1])
            adjacency[edge[1]].append(edge[0])
        
        def dfs(i,parent):
            if i in visited:
                return True
            if i in visiting:
                return False
            
            visiting.add(i)
            for neighbor in adjacency[i]:
                if neighbor == parent:
                    continue
                if not dfs(neighbor,i):
                    return False
            
            visited.add(i)
            visiting.remove(i)
            return True

        if not dfs(0, -1):
            return False
        for i in range(0,n):
            if i not in visited:
                return False
        
        return True
