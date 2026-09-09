class Solution:

    def encode(self, strs: List[str]) -> str:
        fstr = ""
        for word in strs:
            fstr += str(len(word))+"#"+word
        print(fstr)
        return fstr


    def decode(self, s: str) -> List[str]:
        r= 0
        fa = []
        while r <len(s):
            lenword = ''
            while s[r]!="#":
                lenword+=s[r]
                r+=1
            fa.append(s[r+1:r+1 + int(lenword)])
            r =r+ int(lenword)+1
        return fa
