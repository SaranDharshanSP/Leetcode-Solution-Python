class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l,r =0,0
        while r< len(nums):
            if nums[r] != 0:
                nums[r],nums[l] = nums[l],nums[r]
                l+=1
            r+=1
        