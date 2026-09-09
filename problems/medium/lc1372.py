from problems.easy.lc938 import TreeNode


class Solution:
    def dfs(self, root: TreeNode | None) -> list:
        if not root:
            return [-1, -1, -1]
        left, right = self.dfs(root.left), self.dfs(root.right)
        left_path = left[1] + 1
        right_path = right[0] + 1
        return [
            left_path,
            right_path,
            max(left_path, right_path, left[2], right[2]),
        ]

    def longestZigZag(self, root: TreeNode | None) -> int:
        return self.dfs(root)[-1]
