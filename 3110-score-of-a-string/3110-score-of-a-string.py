class Solution:
    def scoreOfString(self, s: str) -> int:
        count = 0
        for i in range(len(s)-1):
            count += abs(ord(s[i])-ord(s[i+1]))
        return count