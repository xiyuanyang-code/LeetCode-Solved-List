#
# @lc app=leetcode id=304 lang=python3
#
# [304] Range Sum Query 2D - Immutable
#

# @lc code=start


# @lc code=start
from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])

        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = matrix[i][j]
                    continue
                if i == 0:
                    dp[i][j] = dp[i][j - 1] + matrix[i][j]
                    continue
                if j == 0:
                    dp[i][j] = dp[i - 1][j] + matrix[i][j]
                    continue

                dp[i][j] = dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - 1] + matrix[i][j]

        self.dp = dp

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 == 0 and col1 == 0:
            return self.dp[row2][col2]
        if row1 == 0:
            return self.dp[row2][col2] - self.dp[row2][col1 - 1]
        if col1 == 0:
            return self.dp[row2][col2] - self.dp[row1 - 1][col2]
        else:
            return (
                self.dp[row2][col2]
                + self.dp[row1 - 1][col1 - 1]
                - self.dp[row1 - 1][col2]
                - self.dp[row2][col1 - 1]
            )


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# @lc code=end


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# @lc code=end
