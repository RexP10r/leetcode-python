from problems.easy.lc938 import TreeNode
from collections import deque


class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        dq = deque()
        dq.append(root)
        ans = 0
        while dq:
            for _ in range(len(dq)):
                root = dq.popleft()
                if root.left:
                    dq.append(root.left)
                if root.right:
                    dq.append(root.right)
            ans += 1
        return ans
