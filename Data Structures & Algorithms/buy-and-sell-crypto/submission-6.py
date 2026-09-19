class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = prices[0]
        p = 0
        for price in range(1,len(prices)):
            p = max(p,prices[price]-minprice)
            minprice = min(minprice,prices[price])
        return p