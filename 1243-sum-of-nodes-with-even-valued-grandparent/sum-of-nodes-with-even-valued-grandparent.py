# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([(root, None, None)])  # (node, parent, grandparent)
        total_sum = 0

        while queue:
            node, parent, grandparent = queue.popleft()

            if grandparent and grandparent.val % 2 == 0:
                total_sum += node.val

            if node.left:
                queue.append((node.left, node, parent))
            if node.right:
                queue.append((node.right, node, parent))

        return total_sum
        