class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        nset = [0]*26
        mset = [0]*26
        for ch in s:
            nset[ord(ch)-ord("a")] +=1
        for c in t:
            mset[ord(c)-ord("a")] +=1
        if nset!=mset:
            return False
        return True
        





        