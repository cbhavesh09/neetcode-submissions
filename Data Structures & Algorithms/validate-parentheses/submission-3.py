class Solution:
    def isValid(self, s: str) -> bool:
        dict1 = {'}':'{',']':'[',')':'('}
        if len(s)<=1:
            return False
        st = []
        for p in s:
            if p in dict1 and st:
                p1 = st.pop()
                if dict1[p]!=p1:
                    return False
            else:
                st.append(p)
        if not st:
            return True
        else:
            return False

        