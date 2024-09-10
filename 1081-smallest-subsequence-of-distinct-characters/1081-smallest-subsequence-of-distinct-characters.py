class Solution:
    def smallestSubsequence(self, s: str) -> str:
        stk=[]
        a= {}
        seen  = set()
        for i in range(len(s)): a[s[i]] = i
        for i in range(len(s)):
            if s[i] in seen: continue
            while stk and stk[-1]> s[i] and a[stk[-1]]>i:
                seen.remove(stk[-1])
                stk.pop()
            stk.append(s[i])
            seen.add(s[i])
        return ''.join(stk)
