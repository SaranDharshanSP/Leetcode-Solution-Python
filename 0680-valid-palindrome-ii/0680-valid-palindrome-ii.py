class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1
        while l<r:
            if s[l] != s[r]:
                skip_l = s[l+1:r+1] == s[l+1:r+1][::-1]
                skip_r = s[l:r] == s[l:r][::-1]
                return  skip_l or skip_r
            l+=1
            r-=1
        return True