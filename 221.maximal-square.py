#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#
from typing import List


# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        current_max = 0
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1 if matrix[i][0] == "1" else 0
            current_max = max(current_max, dp[i][0] ** 2)
        for j in range(n):
            dp[0][j] = 1 if matrix[0][j] == "1" else 0
            current_max = max(current_max, dp[0][j] ** 2)

        for i in range(m):
            for j in range(n):
                if i - 1 >= 0 and j - 1 >= 0 and matrix[i][j] == "1":
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i-1][j-1])
                    current_max = max(current_max, dp[i][j] ** 2)
        return current_max

# @lc code=end
