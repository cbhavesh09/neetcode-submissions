class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = 0
        for price in range(len(prices)):
            for pr in range(1+price,len(prices)):
                if prices[pr]>prices[price]:
                    p = max(p,prices[pr]-prices[price])
        return p
        