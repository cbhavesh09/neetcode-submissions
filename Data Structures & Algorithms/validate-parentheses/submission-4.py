class Solution:
    def isValid(self, s: str) -> bool:
        dict1 = {')': '(', ']': '[', '}': '{'}
        st = []
        for p in s:
            if p in dict1 :
                if not st or st.pop()!= dict1[p]:
                    return False
            else:
                st.append(p)
        return not st


