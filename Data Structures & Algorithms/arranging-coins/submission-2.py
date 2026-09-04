class Solution:
    def arrangeCoins(self, n: int) -> int:
        res = 0
        l,r = 1,n
        while l<=r:
            m = (l+r)//2
            coins = m*(m+1)//2
            if coins>n:
                r = m-1
            else:
                res = max(res,m)
                l = m+1
        return res
        