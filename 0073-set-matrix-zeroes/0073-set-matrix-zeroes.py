class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        s =  []
        n,m= len(matrix), len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    s.append((i,j))
        for i,j in s:
            for k in range(n):
                for l in range(m):
                    matrix[i][l]=0
                    matrix[k][j]=0
        
        
        