class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a ={}

        for i,j in enumerate(nums):
                difference = target - j
                if difference in a: return [a[difference],i]
                a[j] = i
        return []

      


