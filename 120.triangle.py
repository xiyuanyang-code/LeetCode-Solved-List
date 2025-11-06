#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#

# @lc code=start
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        layers = len(triangle)
        dp = [[None] * layers for _ in range(layers)]
        dp[0][0] = triangle[0][0]
        for i in range(1, layers):
            for j in range(i+1):
                if j == 0:
                    dp[i][j] = dp[i-1][j] + triangle[i][0]
                elif j == i:
                    dp[i][j] = dp[i-1][j-1] + triangle[i][-1]
                else:
                    dp[i][j] = min(dp[i-1][j] + triangle[i][j], dp[i-1][j-1] + triangle[i][j])
        return min(dp[layers-1])


# @lc code=end
