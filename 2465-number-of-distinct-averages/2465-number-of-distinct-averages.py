class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        a = set()
        while len(nums)>=2:
            ma = max(nums) 
            nums.remove(ma)
            mi = min(nums)
            nums.remove(mi)
            a.add((ma+mi)/2)
        return len(a)