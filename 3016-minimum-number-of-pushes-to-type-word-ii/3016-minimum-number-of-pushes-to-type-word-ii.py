from collections import Counter
class Solution:
    def minimumPushes(self, word: str) -> int:
        arr = list(Counter(word).values())
        arr.sort(reverse = True)
        res = 0
        for i ,j in enumerate(arr):
            res += j*(i//8 +1)
        return res