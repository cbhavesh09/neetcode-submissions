class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hset = defaultdict(list)
        for word in strs:
            indexList = [0]*26
            for char in word:
                indexList[ord(char)-ord('a')]+=1
            hset[tuple(indexList)].append(word)
        return list(hset.values())

        