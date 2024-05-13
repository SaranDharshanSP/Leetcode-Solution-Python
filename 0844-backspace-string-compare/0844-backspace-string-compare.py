class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def back(s):
            stack =[]
            for i in s:
                if i!='#':
                    stack.append(i)
                elif stack:
                    stack.pop()
            return ''.join(stack)

        return back(s) == back(t)