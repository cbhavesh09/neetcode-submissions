class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1 = [0]*26
        for char in s:
            l1[ord(char)-ord('a')]+=1
        for char in t:
            l1[ord(char)-ord('a')]-=1
        for num in l1:
            if num !=0:
                return False
        return True
        