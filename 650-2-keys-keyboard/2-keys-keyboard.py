class Solution:
    def minSteps(self, n: int) -> int:
        cache = {}
        def dfs(count, clipboard):
            if count == n:
                return 0
            if count > n:
                return float("inf")
            if (count, clipboard) in cache:
                return cache[(count, clipboard)]
            res1 = 1 + dfs(count + clipboard, clipboard)
            res2 = 2  + dfs(count + count, count)
            cache[(count, clipboard)] = min(res1, res2)
            return min(res1, res2)
        if  n == 1:
            return 0
        return 1 + dfs(1, 1)








