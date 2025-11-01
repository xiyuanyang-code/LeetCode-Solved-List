#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#


# @lc code=start
class Solution:
    def calculate(self, n: int):
        if n == 0:
            return 1
        mul = 1
        for i in range(1, n + 1):
            mul *= i
        return mul

    def uniquePaths(self, m: int, n: int) -> int:
        # dp = [[0] * (n) for _ in range(m)]
        # for i in range(m):
        #     dp[i][0] = 1
        # for j in range(n):
        #     dp[0][j] = 1

        # for i in range(1, m):
        #     for j in range(1, n):
        #         dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        # return dp[m - 1][n - 1]

        # or we can calculate C_(m+n-2)^(n-1)
        return int(
            self.calculate(m + n - 2) / (self.calculate(n - 1) * self.calculate(m - 1))
        )


# @lc code=end
