#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#
from typing import List


# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[4e7] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                if i - 1 >= 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j] + grid[i][j])
                if j - 1 >= 0:
                    dp[i][j] = min(dp[i][j], dp[i][j - 1] + grid[i][j])
        return dp[m-1][n-1]


# @lc code=end
