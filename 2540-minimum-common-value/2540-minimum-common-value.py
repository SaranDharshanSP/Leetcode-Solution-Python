class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        left1 = left2 = 0
        right1 , right2 = len(nums1), len(nums2)
        while left1<right1 and left2<right2:
            if nums1[left1] == nums2[left2]:return nums1[left1]
            if nums1[left1] < nums2[left2] : left1+=1
            else: left2+=1
        return -1