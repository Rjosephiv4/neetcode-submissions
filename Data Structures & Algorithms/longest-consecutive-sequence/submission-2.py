class Solution:
    def longestConsecutive(self, nums):
        nums_set = set(nums)

        biggest = 0
        for num in nums_set:
            if num - 1 in nums_set:
                continue

            count = 1
            while num + count in nums_set:
                count += 1

            biggest = max(biggest, count)

        return biggest