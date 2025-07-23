# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)

        # Step 1: Build the undirected graph
        def build_graph(node, parent):
            if not node:
                return
            if parent:
                graph[node.val].append(parent.val)
                graph[parent.val].append(node.val)
            build_graph(node.left, node)
            build_graph(node.right, node)

        build_graph(root, None)

        # Step 2: BFS from target
        visited = set()
        queue = deque([(target.val, 0)])
        res = []

        while queue:
            current, dist = queue.popleft()
            if current in visited:
                continue
            visited.add(current)

            if dist == k:
                res.append(current)
            elif dist < k:
                for neighbor in graph[current]:
                    if neighbor not in visited:
                        queue.append((neighbor, dist + 1))

        return res
