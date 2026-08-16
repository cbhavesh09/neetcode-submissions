class Solution:
    def encode(self, strs: List[str]) -> str:
        strl =""
        for x in strs:
            strl += str(len(x))+ '#'+ x
        return strl

    def decode(self, s: str) -> List[str]:
        l = []
        i = 0
        while i <len(s):
            j = i
            while s[j]!='#':
                j+=1
            length = int(s[i:j])
            l.append(s[j+1:j+1 +length])
            i = j +1 + length
        return l

