class Solution:
    def pivotInteger(self, n: int) -> int:
        tot = n*(n+1)//2
        left = 0
        for i in range(1,n+1):
            tot -=i
            if tot == left : return i
            left+=i
        return -1