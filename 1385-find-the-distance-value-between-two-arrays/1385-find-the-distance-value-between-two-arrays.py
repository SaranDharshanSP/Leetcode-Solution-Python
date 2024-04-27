class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        count = 0
        for num1 in arr1:
            if all(abs(num1 - num2) > d for num2 in arr2):
                count += 1
        return count
