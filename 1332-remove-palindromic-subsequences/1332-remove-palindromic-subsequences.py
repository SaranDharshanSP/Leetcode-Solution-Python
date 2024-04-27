class Solution:
    def removePalindromeSub(self, s: str) -> int:
        p1,p2=0,len(s)-1
        while p1 < p2:
            if s[p1] != s[p2]:
                return 2
            p1+=1
            p2-=1
        return 1