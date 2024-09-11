class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        count = 0
        n = start ^ goal

        while n:
            x = n%2
            if x & 1: count+=1
            n//=2
        return count