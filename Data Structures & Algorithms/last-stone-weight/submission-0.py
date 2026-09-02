class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(0, len(stones)):
            stones[i] = -1 * stones[i]

        heapq.heapify(stones)

        while len(stones) > 1:
            print(stones)
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)

            if stone1 != stone2:
                heapq.heappush(stones, stone1 - stone2)

        return -stones[0] if len(stones) > 0 else 0