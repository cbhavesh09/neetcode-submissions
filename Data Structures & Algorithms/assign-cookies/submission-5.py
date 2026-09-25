class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        lg,ls = 0,0
        while lg<len(g) and ls <len(s):
            if s[ls]>=g[lg]:
                lg+=1
                ls+=1
            else:
                ls+=1
        return lg
        