class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        nums = list(set(nums))
        nums.sort()

        longest = 1
        current = 1

        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                current += 1
            elif nums[i] != nums[i-1]:
                current = 1

            longest = max(longest, current)

        return longest
