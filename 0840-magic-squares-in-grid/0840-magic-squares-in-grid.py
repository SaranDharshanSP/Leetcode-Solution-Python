class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def Valid(i, j):
            nums = [grid[i+x][j+y] for x in range(3) for y in range(3)]
            
            if sorted(nums) != list(range(1, 10)):
                return False
                
            row_sums = [sum(grid[i+x][j+y] for y in range(3)) for x in range(3)]
            col_sums = [sum(grid[i+x][j+y] for x in range(3)) for y in range(3)]
            diag_sums = [grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2], grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j]]

            return all(x == 15 for x in row_sums + col_sums + diag_sums)

        m = len(grid)
        n = len(grid[0])
        if m < 3 or n < 3:
            return 0
        
        count = 0

        for i in range(m - 2):
            for j in range(n - 2):
                if grid[i+1][j+1] == 5 and Valid(i, j):
                    count += 1
        
        return count