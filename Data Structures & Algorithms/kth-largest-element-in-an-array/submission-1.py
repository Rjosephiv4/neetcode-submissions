class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        negative = [-x for x in nums]

        heapq.heapify(negative)

        i=0
        val = None
        while i < k:
            i+=1
            val = heapq.heappop(negative)

        return -val