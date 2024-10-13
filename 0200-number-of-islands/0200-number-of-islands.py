class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def bfs(i,j):
            q = collections.deque()
            visit.add((i,j))
            q.append((i,j))
            while q:
                row,col = q.popleft()
                directions = [(0,1),(1,0),(-1,0),(0,-1)]
                for dr,dc in directions:
                    r,c = dr+row,dc+col
                    if (r in range(rows) and (c in range(cols))
                        and ((r,c) not in visit) and (grid[r][c] == '1')):
                        q.append((r,c))
                        visit.add((r,c))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and (i,j) not in visit:
                    bfs(i,j)
                    islands+=1
        return islands

