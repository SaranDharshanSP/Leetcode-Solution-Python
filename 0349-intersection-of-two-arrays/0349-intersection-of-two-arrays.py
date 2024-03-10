class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a = []
        nums1= set(nums1)
        nums2 = set(nums2)
        for i in nums2:
            if i in nums1 : a.append(i)
        return a