class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        a = len(nums)
        count = 0
        for i in range(a):
            for j in range(i+1,a):
                if nums[i] == nums[j]:
                    count+=1
        return count            
