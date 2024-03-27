class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        a = sorted(set(arr))
        l1 = []
        dc = {}
        for i in range(len(a)):
            dc[a[i]] = i+1
        for i in arr:
            j=dc[i]
            l1.append(j)
        return l1