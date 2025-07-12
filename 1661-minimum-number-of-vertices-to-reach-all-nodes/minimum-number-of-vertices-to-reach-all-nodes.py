class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        incoming = defaultdict(list)
        res = []
        for src, dst in edges:
            incoming[dst].append(src)
        for i in range(n):
            if not incoming[i]:
                res.append(i)
        return res
        