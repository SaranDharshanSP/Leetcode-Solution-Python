class Solution:
    def countSubstrings(self, s: str) -> int:
        def is_palin(sub):
            return sub == sub[::-1]
        count = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                subs = s[i:j + 1]
                if is_palin(subs):
                    count += 1        
        return count