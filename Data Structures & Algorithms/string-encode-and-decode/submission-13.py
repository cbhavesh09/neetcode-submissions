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
            while r < len(s) and s[r]!="#" :
                num+=s[r]
                r+=1
            l+=len(num)+1
            word = s[l:l+int(num)]
            fa.append(word)
            l+=int(num)
        return fa


            

        
