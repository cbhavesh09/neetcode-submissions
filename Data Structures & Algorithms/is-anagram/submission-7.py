class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hset1 = {}
        for char in s:
            hset1[char]= 1+ hset1.get(char,0)
        for ch in t:
            if ch not in hset1:
                return False
            hset1[ch] -= 1
        for ch in hset1:
            if hset1[ch]!=0:
                return False
        return True
        