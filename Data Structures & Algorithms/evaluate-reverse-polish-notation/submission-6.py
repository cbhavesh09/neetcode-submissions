class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        calculations = {"+": lambda a,b: a+b, "-": lambda a,b:a-b, "*": lambda a,b : a*b, "/": lambda a,b : int(a/b) }
        st = []
        for char in tokens:
            if char in calculations:
                a = st.pop()
                b = st.pop()
                c = calculations[char](b,a)
                st.append(c)
                continue
            st.append(int(char))
        return st[0]
            
        