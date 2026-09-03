class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = 0
        for x in range(len(prices)):
            for y in range(1+x,len(prices)):
                profit = prices[y]-prices[x]
                p = max(p,profit)
        return p


        


        