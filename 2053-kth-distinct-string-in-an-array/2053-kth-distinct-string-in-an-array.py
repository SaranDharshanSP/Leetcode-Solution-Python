from collections import Counter
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        c = Counter(arr)
        count  =0
        for i in arr:
            if c[i] == 1:
                count+=1
                if count == k:
                    return i
        return ''
