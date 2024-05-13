class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        l,r=0,1
        while r!=(len(nums)):
            if nums[l] == nums[r]:
                nums[l]*=2
                nums[r]=0
                l+=1
                r+=1
            else:
                l+=1
                r+=1
        l,r = 0,0
        while r< len(nums):
            if nums[r]!= 0:
                nums[l],nums[r]= nums[r],nums[l]
                l+=1
            r+=1
        return nums
            