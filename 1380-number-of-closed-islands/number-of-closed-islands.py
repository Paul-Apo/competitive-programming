class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visit = set()

        def dfs(r, c):
            if (r < 0 or c < 0 or r == rows or c == cols):
                return 0
            if grid[r][c] == 1 or (r, c) in visit:
                return 1
            visit.add((r,c))
            return min(dfs(r, c -1), dfs(r, c+1), dfs(r+1, c), dfs(r-1, c))
        res = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0 and (i,j) not in visit:
                    res += dfs(i, j)
        return res