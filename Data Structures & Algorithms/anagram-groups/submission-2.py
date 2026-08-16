class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        harr = defaultdict(list)
        for word in strs:
            hl = [0]*26
            for ch in word:
                hl[ord(ch)-ord('a')]+=1
            harr[tuple(hl)].append(word)

        return list(harr.values())
        