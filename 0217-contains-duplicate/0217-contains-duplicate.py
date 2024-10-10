class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a = set()
        for i in nums:
            if i not in a: 
                a.add(i)
            else:
                return True
        return False