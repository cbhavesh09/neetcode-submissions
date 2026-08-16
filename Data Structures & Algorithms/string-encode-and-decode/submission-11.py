class Solution:

    def encode(self, strs: List[str]) -> str:
        fs = ""
        for s in strs:
            fs = fs + str(len(s))+"#"+s
        return fs
    def decode(self, s: str) -> List[str]:
        l = 0
        fa = []
        while l <len(s):
            num = ""
            r= l
            word = ""
            while s[r]!="#" and r<len(s)-1:
                num+=s[r]
                r+=1
            l+=len(num)+1
            for x in range(int(num)):
                word+=s[l+x]
            fa.append(word)
            l+=int(num)
        return fa


            

        
