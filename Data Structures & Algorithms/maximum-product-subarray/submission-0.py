class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxVal = nums[0]
        minVal = nums[0]
        answer = nums[0]

        for i in range(1, len(nums)):
            x = nums[i]

            oldMax = maxVal
            oldMin = minVal

            maxVal = max(x, oldMax * x, oldMin * x)
            minVal = min(x, oldMax * x, oldMin * x)

            answer = max(answer, maxVal)

        return answer