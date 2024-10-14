class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = set(nums)
        l = 0

        for i in n:
            if (i-1) not in n:
                l1=1
                while(i+l1) in n:
                    l1+=1
                l = max(l,l1)
        return l
