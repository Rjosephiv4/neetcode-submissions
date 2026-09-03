class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        visiting = set()
        adjacencyList = collections.defaultdict(list)
        for edge in edges:
            adjacencyList[edge[0]].append(edge[1])
            adjacencyList[edge[1]].append(edge[0])

        def dfs(i,parent):
            if i in visiting:
                return 
            visiting.add(i)
            for neighbor in adjacencyList[i]:
                if neighbor ==parent:
                    continue
                dfs(neighbor, i)

            visited.add(i)

        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i,-1)
                count+=1
        return count
