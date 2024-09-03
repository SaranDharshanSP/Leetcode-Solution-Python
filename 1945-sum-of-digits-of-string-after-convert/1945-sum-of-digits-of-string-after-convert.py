class Solution:
    def getLucky(self, s: str, k: int) -> int:
        n = ''.join(str(ord(i) - 96) for i in s)
        
        for i in range(k):
            n = str(sum(int(i) for i in n))
        return int(n)