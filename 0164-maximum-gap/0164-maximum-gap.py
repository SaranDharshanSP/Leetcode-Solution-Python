class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n= len(nums)
        if n == 1 : return 0
        if n == 2: return nums[1] - nums[0]     
        nums.sort()
        mini = 0
        for m in range(1,n) :
            if nums[m]- nums[m-1] > mini :
                mini = nums[m]- nums[m-1]
        return mini