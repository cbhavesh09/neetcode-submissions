class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l=r=0
        length = 0
        hset = set()
        while r<len(s):
            while s[r] in hset:
                hset.remove(s[l])
                l+=1
            hset.add(s[r])
            length = max(length, len(hset))
            r+=1
        return length
        