class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        harr = [0]*26
        for n in s:
            harr[ord(n)-ord('a')]+=1
        for m in t:
            harr[ord(m)-ord('a')]-=1
        if harr == [0]*26:
            return True
        return False
        