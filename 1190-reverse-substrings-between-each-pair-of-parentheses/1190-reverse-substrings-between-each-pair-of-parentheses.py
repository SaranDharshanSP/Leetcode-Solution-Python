class Solution:
    def reverseParentheses(self, s: str) -> str:
        stk = []
        res = []
        for i in range(len(s)):
            if s[i] == '(':
                stk.append(len(res))
            elif s[i] == ')':
                a= stk.pop()
                res[a:] = res[a:][::-1]
            else:
                res.append(s[i])
        return "".join(res)