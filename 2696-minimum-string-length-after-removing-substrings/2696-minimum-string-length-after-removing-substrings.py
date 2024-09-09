class Solution:
    def minLength(self, s: str) -> int:
        stk, rem = [],[ 'AB','CD']
        for i in s:
            stk.append(i)
            if len(stk) >= 2 and stk[-2] + stk[-1] in rem:
                stk.pop()
                stk.pop()
        return len(stk)
                