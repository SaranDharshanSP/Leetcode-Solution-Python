class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        conc = 0
        left = 0
        n = len(nums)
        right = n-1
        while left < right:
            conc += int(str(nums[left]) + str(nums[right]))
            left += 1
            right -= 1
        if n%2!=0:
            conc+=nums[n//2]
        return conc
