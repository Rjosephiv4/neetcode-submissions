class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = [[-1 for i in range(len(heights[0]))] for _ in range(len(heights))]
        atlantic = [[-1 for i in range(len(heights[0]))] for _ in range(len(heights))]

        def dfs(i, j, isPacific):
            if isPacific:
                if pacific[i][j] == 1:
                    return
                pacific[i][j] = 1
            else:
                if atlantic[i][j] == 1:
                    return
                atlantic[i][j] = 1

            if i+1 < len(heights) and heights[i+1][j] >= heights[i][j]:
                dfs(i+1, j, isPacific)
            if i-1 >= 0 and heights[i-1][j] >= heights[i][j]:
                dfs(i-1, j, isPacific)
            if j+1 < len(heights[0]) and heights[i][j+1] >= heights[i][j]:
                dfs(i, j+1, isPacific)
            if j-1 >= 0 and heights[i][j-1] >= heights[i][j]:
                dfs(i, j-1, isPacific)

        for j in range(len(heights[0])):
            dfs(0, j, False)  # Pacific top
        for i in range(len(heights)):
            dfs(i, 0, False)  # Pacific left

        for i in range(len(heights)):
            dfs(i, len(heights[0])-1 , True)  # Atlantic right
        for j in range(len(heights[0])):
            dfs(len(heights) -1 , j, True)  # Atlantic bottom

        output = []

        for i in range(len(heights)):
            for j in range(len(heights[0]) ):
                if atlantic[i][j] == 1 and pacific[i][j] == 1:
                    output.append([i, j])
        return output