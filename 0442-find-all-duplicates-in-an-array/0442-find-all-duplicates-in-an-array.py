class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.sort()
        a=[]
        for i in range(1,len(nums)):
            if nums[i-1] == nums[i]: a.append(nums[i])
        return a