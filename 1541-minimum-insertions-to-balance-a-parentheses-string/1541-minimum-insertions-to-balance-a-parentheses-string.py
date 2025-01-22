class Solution:
    def minInsertions(self, s: str) -> int:
        stk = []
        res = 0
        i = 0
        while i < len(s):
            if s[i] == '(':
                stk.append('(')
            elif s[i] == ')':
                if i+1<len(s) and s[i+1] ==')': i+=1
                else:res+=1
                if stk: stk.pop()
                else: res += 1
            i+=1
        res +=(len(stk) *2)
        return res
