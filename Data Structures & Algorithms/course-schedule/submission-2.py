class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        visiting = set()
        visited = set()
        listOfCourses = collections.defaultdict(list)
        for prerequsite in prerequisites:
            listOfCourses[prerequsite[0]].append(prerequsite[1])
        
        def dfs(i,visiting):
            if i in visiting:
                return False
            if i in visited:
                return True
            
            
            if len(listOfCourses[i]) == 0:
                return True
            
            visiting.add(i)
            for prereq in listOfCourses[i]:
                if not dfs(prereq, visiting):
                    return False
            visiting.remove(i)
            visited.add(i)
            return True

        for i in range(numCourses):
            if not dfs(i,visiting):
                return False
        return True