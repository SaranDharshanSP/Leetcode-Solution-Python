class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a = set()
        count = 0
        l = 0
        for r in range(len(s)):
            while s[r] in a:
                a.remove(s[l])
                l+=1
            a.add(s[r])
            count = max(count, r-l+1)
        return count
            