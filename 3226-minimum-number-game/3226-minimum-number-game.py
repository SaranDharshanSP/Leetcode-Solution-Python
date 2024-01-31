class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        for i in range(1,len(nums),2):
            nums[i],nums[i-1]= nums[i-1],nums[i]
        return nums    