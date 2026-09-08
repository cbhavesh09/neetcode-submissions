class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        listch = [0]*26
        for ch in s:
            listch[ord(ch)-ord('a')]+=1
        for char in t:
            if listch[ord(char)-ord('a')]==0:
                return False
            listch[ord(char)-ord('a')]-=1
        for freq in listch:
            if freq>0:
                return False
        return True
            
