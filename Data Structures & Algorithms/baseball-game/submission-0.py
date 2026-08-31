class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st = []
        fans = 0
        for el in operations:
            if el == 'C':
                st.pop()
            elif el == '+':
                ans = int(st[-1])+int(st[-2])
                st.append(ans)
            elif el == 'D':
                an = 2*int(st[-1])
                st.append(an)
            else:
                st.append(el)
        print(st)
        for num in st:
            fans+=int(num)
        return fans


        