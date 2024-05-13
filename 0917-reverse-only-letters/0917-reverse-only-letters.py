class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        a = [b for b in s if b.isalpha()]
        a = a[::-1]
        res = []
        j = 0
        for i in range(len(s)):
            if s[i].isalpha():
                res.append(a[j]) 
                j += 1
            else:
                res.append(s[i])
        return ''.join(res)  

