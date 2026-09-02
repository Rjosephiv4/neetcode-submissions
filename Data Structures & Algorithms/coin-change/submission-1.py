class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        subs = (amount +1) * [float('inf')]
        subs[0]= 0
        for coin in coins:
            if coin < amount+1:
                subs[coin] = 1
        
        for j in range(0, len(subs)):
            for denom in coins:
                if j - denom > 0 and subs[j-denom]:
                    subs[j] = min(subs[j],subs[j-denom] + 1)
        
        return subs[amount] if subs[amount] != float('inf') else -1


