class Solution:
    def numSquares(self, n: int) -> int:
        if n <= 0:
            return 0
        dp: list[int] = [0]
        for _ in range(n):
            m = len(dp)
            count_sqrs = 65_536
            i = 1
            while i * i <= m:
                count_sqrs = min(count_sqrs, dp[m - i * i] + 1)
                i += 1
            dp.append(count_sqrs)
        return dp[n]
