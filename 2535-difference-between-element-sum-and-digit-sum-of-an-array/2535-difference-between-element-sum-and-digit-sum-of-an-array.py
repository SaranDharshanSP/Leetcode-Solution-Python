class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        s = sum(nums)
        a = "".join(map(str, nums)) 
        su = 0
        for i in a:
            su += int(i)
        return s - su
