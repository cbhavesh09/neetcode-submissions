class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l=r=0
        fs=""
        while r<len(word2) and l<len(word1):
            fs+=word1[l] +word2[r]
            r+=1
            l+=1
        if r<len(word2):
            fs+=word2[r:]
        if l<len(word1):
            fs+=word1[l:]
        return fs
        

        