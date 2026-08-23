class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)==len(t):
            hset1 = {}
            hset2 = {}
            for ch in s:
                hset1[ch] = 1+ hset1.get(ch,0)
            for c in t:
                hset2[c] = 1+ hset2.get(c,0)
            if hset1 == hset2:
                return True
        return False
        
        