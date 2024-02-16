class Solution:
    def firstUniqChar(self, s: str) -> int:
        unique = dict()

        for i in s:
            unique[i] = unique.get(i,0) + 1

        for i in range(len(s)):
            if unique[s[i]] == 1: return i
        
        return -1