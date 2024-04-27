class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        if arr.count(0) >= 2:
            return True
        arr_set = set(arr)
        for num in arr_set:
            if num != 0 and num * 2 in arr_set:
                return True
        return False