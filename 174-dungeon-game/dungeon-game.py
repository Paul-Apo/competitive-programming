class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        
        # dp array with extra row and column filled with infinity
        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        
        # base case: need at least 1 health to survive at princess cell
        dp[m][n-1] = dp[m-1][n] = 1
        
        # fill dp from bottom-right to top-left
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                need = min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j]
                dp[i][j] = max(1, need)
        
        return dp[0][0]
        