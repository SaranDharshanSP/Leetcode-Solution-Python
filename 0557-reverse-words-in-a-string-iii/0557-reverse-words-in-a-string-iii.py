class Solution:
    def reverseWords(self, s: str) -> str:
        S = s.split(' ')
        r = [i[::-1] for i in S]
        return ' '.join(r)