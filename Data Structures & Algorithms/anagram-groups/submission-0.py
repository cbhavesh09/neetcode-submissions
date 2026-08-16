class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d_set = defaultdict(list)
        for word in strs:
            count =[0]*26
            for letter in word:
                pos = ord(letter)-ord('a')
                count[pos]+=1
            d_set[tuple(count)].append(word)
        return list(d_set.values())
