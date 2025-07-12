from collections import deque
from typing import List

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        directions = {
            1: {'left', 'right'},
            2: {'up', 'down'},
            3: {'left', 'down'},
            4: {'right', 'down'},
            5: {'left', 'up'},
            6: {'right', 'up'}
        }
        
        # Movement deltas
        moves = {
            'up': (-1, 0),
            'down': (1, 0),
            'left': (0, -1),
            'right': (0, 1)
        }
        
        # Which direction connects to what
        opposites = {
            'up': 'down',
            'down': 'up',
            'left': 'right',
            'right': 'left'
        }
        
        visited = [[False]*n for _ in range(m)]
        queue = deque([(0, 0)])
        visited[0][0] = True
        
        while queue:
            i, j = queue.popleft()
            if i == m-1 and j == n-1:
                return True
            
            for dir, (di, dj) in moves.items():
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and not visited[ni][nj]:
                    if dir in directions[grid[i][j]] and opposites[dir] in directions[grid[ni][nj]]:
                        visited[ni][nj] = True
                        queue.append((ni, nj))
                        
        return False
