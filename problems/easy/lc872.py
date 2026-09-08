from problems.easy.lc938 import TreeNode


class Solution:
    def get_leafs_seq(self, root: TreeNode | None) -> list:
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        return self.get_leafs_seq(root.left) + self.get_leafs_seq(root.right)

    def leafSimilar(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:
        return self.get_leafs_seq(root1) == self.get_leafs_seq(root2)
