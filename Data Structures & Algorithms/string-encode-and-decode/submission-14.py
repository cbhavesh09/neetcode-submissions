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
            r= l
            while s[r] != "#":
                r+=1
            length = int(s[l:r])
            fa.append(s[r+1:r+1+length])
            l= length + r +1
        return fa


            

        
