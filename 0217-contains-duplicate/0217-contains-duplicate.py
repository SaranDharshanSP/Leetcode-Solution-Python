class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a = set()
        for i in range(len(nums)):
            if nums[i] not in a:
                    a.add(nums[i])
            else: return True
        return False