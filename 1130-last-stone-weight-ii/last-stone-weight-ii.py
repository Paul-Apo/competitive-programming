class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        sumStones = sum(stones)
        target = ceil(sumStones / 2)
        dp = {}
        def dfs(i, total):
            if i == len(stones) or total >= target:
                return abs(total - (sumStones - total))
            if (i, total) in dp:
                return dp[(i, total)]            
            dp[(i, total )] = min(
                dfs(i +1, total),
                dfs(i+1, total + stones[i])
            )
            return dp[(i, total)]
        return dfs(0, 0)
    
        