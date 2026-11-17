class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s)!=len(t):
            return False
        l1 = [0 for _ in range(26)]
        
        for ch in s:
            l1[ord(ch)-ord('a')]+=1
        for c in t:
            l1[ord(c)-ord('a')]-=1

        fset = set(l1)
        if len(fset)==1 :
            return True
        else:
            return False
        
        