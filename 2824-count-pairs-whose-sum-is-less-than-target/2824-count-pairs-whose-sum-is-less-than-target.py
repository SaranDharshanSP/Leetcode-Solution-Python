class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        count = 0
        nums = sorted(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if 0 <= i < j and nums[i] + nums[j] < target:
                    count+=1
        return count            
