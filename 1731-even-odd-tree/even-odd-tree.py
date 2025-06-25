# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        queue = deque([root])
        level = 0

        while queue:
            level_size = len(queue)
            prev_value = None

            for _ in range(level_size):
                node = queue.popleft()
                value = node.val

                # Parity check
                if level % 2 == 0:
                    if value % 2 == 0:
                        return False
                    if prev_value is not None and value <= prev_value:
                        return False
                else:
                    if value % 2 == 1:
                        return False
                    if prev_value is not None and value >= prev_value:
                        return False

                prev_value = value

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            level += 1

        return True