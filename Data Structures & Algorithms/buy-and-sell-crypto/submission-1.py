class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = 0
        for x in range(len(prices)):
            for y in range(x+1,len(prices)):
                tp = prices[y]-prices[x]
                p = max(p,tp)
        return p
        