class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mapnum = {}
        for num in nums:
            if num in mapnum:
                mapnum[num] +=1
            else:
                mapnum[num] = 1
        
        biggest = 0
        for num in nums:
            if num - 1 in nums:
                continue
            count = 1
            while num + count in nums:
                count += 1
            biggest = max(biggest,count)
        return biggest