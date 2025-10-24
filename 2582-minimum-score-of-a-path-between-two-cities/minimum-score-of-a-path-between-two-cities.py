class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)
        for  src, dst, distance in roads:
            adj[src].append((dst, distance))
            adj[dst].append((src, distance))
        visit = set()
        res = float("inf")
        def dfs(i):
            if i in visit:
                return 
            visit.add(i)
            nonlocal res
            for nei, distance in adj[i]:
                res = min(res, distance)
                dfs(nei)
        dfs(1)
        return res

        