class Solution:
    def isValid(self, s: str) -> bool:
        st = deque()

        for c in s:
            if c == '(' or c == '{' or c == '[':
                st.append(c)
            elif st and ((c == ')' and st[-1] == '(') or (c == '}' and st[-1] == '{') or (st[-1]== '[' and c == ']')):
                st.pop()
            else:
                return False
        
        return not st
