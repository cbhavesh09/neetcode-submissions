class Solution:

    def encode(self, strs: List[str]) -> str:
        fs = ""
        for word in strs:
            n = len(word)
            fs+=str(n)+"#"+word
        return fs

    def decode(self, s: str) -> List[str]:
        fl = []
        i = 0
        while i <len(s):
            j = i
            while s[j ]!= "#":
                j+=1
            length = int(s[i:j])
            fl.append(s[j+1:j+length+1])
            i = j+length+1
        return fl
        