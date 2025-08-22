class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]   # 4-direction moves
        q = deque()

        # ---------- 1. Depth-first search: mark first island ----------
        def dfs(r, c):
            if r < 0 or r >= n or c < 0 or c >= n:     # outside grid
                return
            if grid[r][c] != 1:                        # already water or painted
                return
            grid[r][c] = 2                             # mark as part of first island
            q.append((r, c))                           # enqueue for later BFS
            for dr, dc in dirs:                        # visit 4 neighbours
                dfs(r + dr, c + dc)

        # find any land-cell to start DFS
        done = False
        for i in range(n):
            if done: break
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)                # paint entire first island
                    done = True
                    break                       # exit loops once painted

        # ---------- 2. Breadth-first search: expand until 2nd island ----------
        steps = 0                               # BFS layer counter
        while q:
            for _ in range(len(q)):             # process one layer
                x, y = q.popleft()
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n:
                        if grid[nx][ny] == 1:   # reached second island
                            return steps
                        if grid[nx][ny] == 0:   # water → flip & expand
                            grid[nx][ny] = 2
                            q.append((nx, ny))
            steps += 1                          # next ring costs +1 flip