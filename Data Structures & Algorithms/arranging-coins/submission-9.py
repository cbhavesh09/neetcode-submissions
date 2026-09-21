class Solution:
    def arrangeCoins(self, n: int) -> int:
        l,r = 1,n
        maxpos = 0
        while l<=r:
            pos = (l+r)//2
            coins = pos*(pos+1)//2
            if coins>n:
                r = pos-1
            else:
                l = pos+1
                maxpos = max(maxpos,pos)
        return maxpos
        
        