from problems.easy.lc938 import TreeNode
from collections import deque


class Solution:
    def rightSideView(self, root: TreeNode | None) -> list:
        if not root:
            return []
        queue = deque()
        queue.append(root)
        res = []
        while queue:
            cur_len = len(queue)
            for i in range(cur_len):
                node = queue.popleft()
                if i == cur_len - 1:
                    res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res
