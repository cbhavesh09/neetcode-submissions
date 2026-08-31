class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st = []
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
                st.append(int(el))
        return sum(st)


        