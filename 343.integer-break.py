#
# @lc app=leetcode id=343 lang=python3
#
# [343] Integer Break
#


# @lc code=start
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            dp[i][1] = i

        for i in range(1, n + 1):
            for k in range(1, i + 1):
                for select in range(1, i - k + 2):
                    dp[i][k] = max(dp[i][k], select * dp[i - select][k - 1])

        res = 0
        for k in range(2, n+1):
            res = max(res, dp[n][k])
        return res


# @lc code=end
