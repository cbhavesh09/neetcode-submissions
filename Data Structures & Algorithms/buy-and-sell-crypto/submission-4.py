class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mxprofit = 0
        mprice = prices[0]
        for num in range(1,len(prices)):
            mxprofit = max(mxprofit,prices[num]-mprice)
            mprice = min(prices[num],mprice)
        return mxprofit
       


        


        