class Solution:
    def largestGoodInteger(self, num: str) -> str:
        a = [3*str(i) for i in range(9,-1,-1)]
        for i in a:
            if i in num: return i
        return ''