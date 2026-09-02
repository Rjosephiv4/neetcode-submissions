class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_amount = 0 

        n = len(prices)

        for i in range(0, n):
            for j in range(i+1,n):
                if prices[j] - prices[i] > max_amount:
                    max_amount = prices[j] - prices[i]
        return max_amount