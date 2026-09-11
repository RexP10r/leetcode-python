from problems.easy.lc938 import TreeNode


class Solution:
    def get_inorder_succ(self, root: TreeNode) -> TreeNode:
        curr = root.right
        while curr and curr.left:
            curr = curr.left
        return curr

    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:
        if not root:
            return None

        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            succ = self.get_inorder_succ(root)
            root.val = succ.val
            root.right = self.deleteNode(root.right, succ.val)
        return root
