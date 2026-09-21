class Solution:
    def arrangeCoins(self, n: int) -> int:
        l,r = 1, n
        maxv = 0
        while l<=r:
            m = (l+r)//2
            coins = m*(m+1)//2
            if coins>n:
                r = m-1
            else :
                maxv = max(m,maxv)
                l = m+1
        return maxv
        
        