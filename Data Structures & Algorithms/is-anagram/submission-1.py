class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lista = [0]*26
        listb = [0]*26
        for ch in s:
            lista[ord(ch)-ord('a')]+=1
        for ch in t:
            listb[ord(ch)-ord('a')]+=1
        if lista == listb:
            return True
        return False


        