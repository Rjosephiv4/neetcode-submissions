class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def helper(start, end):
            pivot = end
            i = start
            swapper = start

            while i < end:
                if nums[i] > nums[pivot]:
                    i+=1
                    continue
                nums[i], nums[swapper] = nums[swapper], nums[i]
                i+=1
                swapper+=1

            nums[pivot], nums[swapper] = nums[swapper], nums[pivot]

            return swapper


        result = -1

        start1 = 0
        end1 = len(nums) - 1
        while result != len(nums)-k:
            result = helper(start1, end1)

            if result == len(nums)-k:
                return nums[len(nums)-k]
            elif result < len(nums)-k:
                start1 = result+1
            else:
                end1 = result-1

        