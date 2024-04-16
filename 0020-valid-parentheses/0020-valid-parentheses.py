class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        para = { ")":"(", "]":"[", "}":"{"}
        for i in s:
            if i in para:
                if stack and stack[-1] == para[i]:
                    stack.pop()
                else: 
                    return False
            else:
                stack.append(i)
        return True if not stack else False