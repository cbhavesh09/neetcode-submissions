class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2) : return False
        s1List = [0]*26
        s2List = [0]*26

        for i in range(len(s1)):
            s1List[ord(s1[i])-ord('a')]+=1
            s2List[ord(s2[i])-ord('a')]+=1
        matches = 0

        for k in range(26):
            matches +=(1 if s1List[k]==s2List[k] else 0)
        l = 0
        for j in range(len(s1),len(s2)):
            if matches == 26: return True
            index = ord(s2[j])- ord('a')
            s2List[index]+=1
            if s1List[index]==s2List[index]:
                matches+=1
            elif s1List[index]+1== s2List[index]:
                matches-=1
            index = ord(s2[l])- ord('a')
            s1List[index]+=1
            if s1List[index]==s2List[index]:
                matches+=1
            elif s1List[index]-1== s2List[index]:
                matches-=1
            l+=1
        return matches == 26

            

        
        