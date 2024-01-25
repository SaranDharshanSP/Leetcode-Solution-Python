class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d1 = {}
        for key, val in enumerate(nums):
            if val not in d1:
                d1[val] = key
            else:
                if abs(d1.get(val) - key) <= k:
                    return True
                else:
                    d1[val] = key

        return False