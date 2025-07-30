# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node, depth):
            # Base case: if node is None, return None and depth
            if not node:
                return None, depth
            
            # Recurse on left and right subtrees
            left_lca, left_depth = dfs(node.left, depth + 1)
            right_lca, right_depth = dfs(node.right, depth + 1)
            
            # If depths are equal, current node is LCA
            if left_depth == right_depth:
                return node, left_depth
            # Return the LCA from deeper subtree
            elif left_depth > right_depth:
                return left_lca, left_depth
            else:
                return right_lca, right_depth
        
        # Return only the LCA node from the result
        lca, _ = dfs(root, 0)
        return lca
