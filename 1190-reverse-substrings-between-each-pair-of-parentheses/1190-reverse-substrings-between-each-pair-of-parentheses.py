class Solution:
    def reverseParentheses(self, s: str) -> str:
        stk = []
        for ch in s:
            if ch != ')':
                stk.append(ch)
            else:
                ls = []
                while stk and stk[-1] != '(':
                    ls.append(stk.pop())
                if stk:
                    stk.pop()
                stk += ls
        return "".join(stk)