class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        max_val = float("-inf")

        def dfs(node) -> int:
            nonlocal max_val
            if node is None:
                return 0

            left_gain = max(0, dfs(node.left))
            right_gain = max(0, dfs(node.right))

            max_val = max(max_val, node.val + left_gain + right_gain)

            return node.val + max(left_gain, right_gain)

        dfs(root)

        return max_val
