class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        root = list(range(n + 1))
        size = [1] * (n + 1)

        def find(x):
            while x != root[x]:
                root[x] = root[root[x]]
                x = root[x]
            return root[x]
        
        def union(x, y):
            root_x = find(x)
            root_y = find(y)

            if root_x != root_y:
                if size[root_x] > size[root_y]:
                    root[root_y] = root_x
                    size[root_x] += size[root_y]
                else:
                    root[root_x] = root_y
                    size[root_y] += size[root_x]
        
        result = []
        for x, y in edges:
            if find(x) == find(y):
                result = [x, y]
            else:
                union(x, y)
        result7 = result
        return result7