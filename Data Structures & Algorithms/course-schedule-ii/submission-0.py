class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        visiting = set()
        visited = set()
        listOfCourses = collections.defaultdict(list)
        for prerequsite in prerequisites:
            listOfCourses[prerequsite[0]].append(prerequsite[1])
        output = []
        def dfs(i,visiting):
            if i in visiting:
                return False
            if i in visited:
                return True
            
            
            if len(listOfCourses[i]) == 0:
                visited.add(i)
                output.append(i)
                return True
            
            visiting.add(i)
            for prereq in listOfCourses[i]:
                if not dfs(prereq, visiting):
                    return False
            visiting.remove(i)
            visited.add(i)
            output.append(i)
            return True

        for i in range(numCourses):
            if not dfs(i,visiting):
                return []
        return output