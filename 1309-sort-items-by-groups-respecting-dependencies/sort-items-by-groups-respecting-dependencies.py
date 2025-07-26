class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        # Step 1: Assign unique group ID to ungrouped items
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1

        # Build item and group graphs
        item_graph = defaultdict(list)
        item_indegree = [0] * n
        group_graph = defaultdict(list)
        group_indegree = [0] * m

        for curr in range(n):
            for prev in beforeItems[curr]:
                item_graph[prev].append(curr)
                item_indegree[curr] += 1
                if group[prev] != group[curr]:
                    group_graph[group[prev]].append(group[curr])
                    group_indegree[group[curr]] += 1

        def topo_sort(graph, indegree, nodes):
            res = []
            queue = deque([node for node in nodes if indegree[node] == 0])
            while queue:
                u = queue.popleft()
                res.append(u)
                for v in graph[u]:
                    indegree[v] -= 1
                    if indegree[v] == 0:
                        queue.append(v)
            return res if len(res) == len(nodes) else []

        item_order = topo_sort(item_graph, item_indegree, list(range(n)))
        if not item_order:
            return []

        group_order = topo_sort(group_graph, group_indegree, list(range(m)))
        if not group_order:
            return []

        # Group items by group id in order of item_order
        group_to_items = defaultdict(list)
        for item in item_order:
            group_to_items[group[item]].append(item)

        # Concatenate items in group order
        res = []
        for g in group_order:
            res.extend(group_to_items[g])
        return res
        