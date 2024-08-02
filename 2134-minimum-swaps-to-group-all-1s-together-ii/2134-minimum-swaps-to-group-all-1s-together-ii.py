class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        total = nums.count(1)
        count = nums[-total:].count(1)
        ans = total - count

        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            if nums[i-total] == 1:
                count -= 1
            if count == total: return 0
            ans = min(ans, total-count)

        return ans