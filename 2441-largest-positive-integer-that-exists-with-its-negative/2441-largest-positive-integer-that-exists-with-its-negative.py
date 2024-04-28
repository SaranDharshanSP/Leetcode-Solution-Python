class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        seen = set(nums)
        l = float('-inf')

        for i in nums:
            if -i in seen:
                l = max(l,i)
        return l if l!=float('-inf') else -1
            
