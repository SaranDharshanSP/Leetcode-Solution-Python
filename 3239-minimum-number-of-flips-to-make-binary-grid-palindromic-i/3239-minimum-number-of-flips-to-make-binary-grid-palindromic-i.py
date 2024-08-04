class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        def rows():
            total = 0
            for row in grid:
                for i in range(n // 2):
                    if row[i] != row[n - 1 - i]:
                        total += 1
            return total
        
        def col():
            total = 0
            for col in range(n):
                for i in range(m // 2):
                    if grid[i][col] != grid[m - 1 - i][col]:
                        total += 1
            return total
        
        return min(rows(), col())