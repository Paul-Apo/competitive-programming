class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        k = 2  # at most two transactions

        dp = [[0] * n for _ in range(k + 1)]

        for t in range(1, k + 1):
            max_diff = -prices[0]  # best dp[t-1][m] - prices[m] so far
            for d in range(1, n):
                # either skip today or sell today using best buy point
                dp[t][d] = max(dp[t][d - 1], prices[d] + max_diff)
                # update max_diff for next days
                max_diff = max(max_diff, dp[t - 1][d] - prices[d])

        return dp[k][n - 1]