class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode | None, low: int, high: int) -> int:
        stack = [root]
        res = 0
        while stack:
            node = stack.pop()
            if node:
                value = node.val
                if value < high:
                    stack.append(node.right)
                if value > low:
                    stack.append(node.left)
                if low <= value <= high:
                    res += value
        return res
