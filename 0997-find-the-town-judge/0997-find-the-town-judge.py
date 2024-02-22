class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        con = [0]*(n+1)
        for i in trust:
            con[i[0]]-=1
            con[i[1]]+=1
            
        for i in range(1,n+1):
            if con[i] ==n-1:
                return i
        return -1