class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = prices[0]
        for num in range(1,len(prices)):
            profit = max(profit,prices[num]-min_price)
            min_price = min(min_price,prices[num])
        return profit
        