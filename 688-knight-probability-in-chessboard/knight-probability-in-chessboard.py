class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        deltas = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
        prev = [[0.0] * n for _ in range(n)]
        prev[row][column]= 1
        for _ in range(k):
            cur = [[0.0] * n for _ in range(n)]
            for x in range(n):
                for y in range(n):
                    if prev[x][y] > 0:
                        for dx, dy in deltas:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < n and 0 <= ny < n:
                                 cur[nx][ny] += prev[x][y] / 8
            prev = cur
        return sum(sum(r) for r in prev)

        