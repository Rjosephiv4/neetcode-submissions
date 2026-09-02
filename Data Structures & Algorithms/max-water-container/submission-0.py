class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) -1 

        biggest = float('-inf')

        while left < right:
            total = min(heights[left], heights[right]) * (right-left)
            if total > biggest:
                biggest = total
            if heights[left] < heights[right]:
                left+=1
            else:
                right-=1

        return biggest