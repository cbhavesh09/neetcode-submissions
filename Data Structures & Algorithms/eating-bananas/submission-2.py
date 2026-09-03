class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        while l<=r:
            m = (l+r)//2
            th = 0
            for num in piles:
                th += (num+m-1)//m
            if th <=h :
                r = m-1
            else:
                l = m+1
        return l