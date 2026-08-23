class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hset = {}
        for ch in s:
            hset[ch]= hset.get(ch,0)+1
        for c in t:
            hset[c]= hset.get(c,0)-1
        for char in hset:
            if hset[char]!=0:
                return False
        return True