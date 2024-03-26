class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        nums_set.discard(0)
        
        missing = 1
        while missing in nums_set:
            missing += 1
        
        return missing
