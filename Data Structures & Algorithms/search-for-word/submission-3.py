class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #loop through the each element and if we hit the first letter than start
        #branching 
 
        def search(i,j,curr,visited,l):
            if word == curr:
                return True
           
            if i >= len(board) or i < 0:
                return False
            if j >= len(board[0]) or j < 0:
                return False
            if (i,j) in visited: 
                return False
            if word[l] != board[i][j]:
                return False

            curr+=board[i][j]
            visited.add((i,j))

            found =  search(i+1,j,curr,visited,l+1) or search(i-1,j,curr,visited,l+1) or search(i, j+1, curr,visited,l+1) or search(i, j-1, curr,visited,l+1)

            visited.remove((i,j))
            return found

        for i in range(0,len(board)):
            for j in range(0,len(board[0])):
                visited = set()
                if board[i][j] == word[0]:
                    if search(i,j,"",visited,0):
                        return True
        return False