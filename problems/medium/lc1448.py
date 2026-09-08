from problems.easy.lc938 import TreeNode


class Solution:
    def dfs(self, root: TreeNode | None, prev: int) -> int:
        if not root:
            return 0
        res = 0
        if prev <= root.val:
            res = 1
            prev = root.val
        return res + self.dfs(root.left, prev) + self.dfs(root.right, prev)

    def goodNodes(self, root: TreeNode | None) -> int:
        return self.dfs(root, root.val)
