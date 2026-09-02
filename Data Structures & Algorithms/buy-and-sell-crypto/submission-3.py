class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_amount = 0 

        l = 0
        
        for r in range(1,len(prices)):
            while prices[r] - prices[l] > max_amount:
                max_amount = prices[r] - prices[l]
            
            if prices[r] < prices[l]:
                l = r
        
        return max_amount