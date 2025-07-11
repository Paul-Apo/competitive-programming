class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        if source == destination:
            return True
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        seen = set()
        def dfs(i):
            if i == destination:
                return True
            for neigh_node in graph[i]:
                if neigh_node not in seen:
                    seen.add(neigh_node)                
                    if dfs(neigh_node):
                        return True
            return False
        
        return dfs(source)

        