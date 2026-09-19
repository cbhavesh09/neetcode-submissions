class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=r= 0
        length = 0
        hset = set()
        while r < len(s):
            if s[r] in hset:
                while s[r] in hset:
                    hset.remove(s[l])
                    l+=1
            hset.add(s[r])
            r+=1
            length = max(length,len(hset))
        return length


        