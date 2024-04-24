class Solution:
    def tribonacci(self, n: int) -> int:
        if n ==0 : return 0
        if n ==1 or n==2 : return 1
        ab =[0]*(n+1)
        ab[0] = 0
        ab[1] = 1
        ab[2] = 1
        for i in range(3,n+1):
            ab[i] = ab[i-1] +ab[i-2] +ab[i-3]
        return ab[n]