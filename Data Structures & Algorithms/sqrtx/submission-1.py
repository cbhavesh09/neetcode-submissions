class Solution:
    def mySqrt(self, x: int) -> int:
        l,r = 0,x
        sqr = 0
        while l <= r:
            m = (l+r)//2
            if m *m == x:
                return m
            elif m*m >x:
                r = m-1
            elif m*m <x:
                sqr = m
                l = m+1
        return sqr
        
        