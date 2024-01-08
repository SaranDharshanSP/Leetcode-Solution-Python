class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n= len(nums)
        a = (-min(nums))
        nums = [i+a for i in nums]
        for i in range(len(str(max(nums)))):
            C = [0]*10
            B = [0]*n
            for j in range(n):
                x = int(nums[j]/(10**i)%10)
                C[x] += 1
            for k in range(1,10):
                C[k] = C[k] + C[k-1]
            for l in range(n-1,-1,-1):
                x = int(nums[l]/(10**i)%10)
                C[x] -= 1
                B[C[x]] = nums[l]
            nums = B
        nums = [i-a for i in nums]
        return nums   