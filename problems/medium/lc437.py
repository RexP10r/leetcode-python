from problems.easy.lc938 import TreeNode


class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        ans = 0
        freq = {0: 1}

        def dfs(root: TreeNode | None, prefix_sum: int):
            if not root:
                return
            nonlocal ans

            prefix_sum += root.val
            if prefix_sum - targetSum in freq:
                ans += freq[prefix_sum - targetSum]
            freq[prefix_sum] = freq.get(prefix_sum, 0) + 1

            dfs(root.left, prefix_sum)
            dfs(root.right, prefix_sum)

            freq[prefix_sum] -= 1

        dfs(root, 0)
        return ans
