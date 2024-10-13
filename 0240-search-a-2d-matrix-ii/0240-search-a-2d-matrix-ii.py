class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i,j = 0, len(matrix[0])-1
        while i>=0 and i<len(matrix) and j>=0 and len(matrix[0]):
            if matrix[i][j]==target: 
                return True
            elif matrix[i][j]>target : j-=1
            else:i+=1
        return False