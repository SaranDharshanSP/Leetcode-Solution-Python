class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        neg = []
        pos = []
        r = []
        for num in nums :
            if num > 0: pos.append(num)
            else: neg.append(num)
        i=0
        while i<len(neg):
            r.append(pos[i])
            r.append(neg[i])
            i+=1
        return r
