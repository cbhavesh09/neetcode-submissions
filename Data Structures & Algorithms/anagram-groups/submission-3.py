class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hset = defaultdict(list)
        fa = []
        for word in strs:
            indexList = [0]*26
            for ch in word:
                indexList[ord(ch)-ord('a')]+=1
            hset[tuple(indexList)].append(word)
        for lists in hset.values():
            fa.append(lists)
        return fa
        
        