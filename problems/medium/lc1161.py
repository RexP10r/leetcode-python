from problems.easy.lc938 import TreeNode


class Solution:
    def maxLevelSum(self, root: TreeNode | None) -> int:
        if not root:
            return 1
        queue = [root]
        max_sum = float("-inf")
        min_level = 0
        cur_level = 0
        while queue:
            cur_level += 1
            cur_sum = 0
            temp = []
            for node in queue:
                cur_sum += node.val
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            if cur_sum > max_sum:
                max_sum = cur_sum
                min_level = cur_level
            queue = temp
        return min_level
