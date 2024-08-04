class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        res = []
        j=0
        while j < len(nums):
            pre_sum = 0
            for i in range(j,len(nums)):
                pre_sum += nums[i]
                res.append(pre_sum)
            j+=1
        res.sort()
        
        ans=0
        for i in range(left-1,right):
            ans+= res[i]
        return ans% 1000000007