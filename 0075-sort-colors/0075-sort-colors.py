class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a = {0:0, 1:0, 2:0}
        for i in nums:
            a[i]+=1

        i=0
        for j in [0,1,2]:
            for k in range(a[j]):
                nums[i]=j
                i+=1


