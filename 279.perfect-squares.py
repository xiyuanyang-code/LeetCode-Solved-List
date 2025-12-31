#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#
import math


# @lc code=start
class Solution:
    # def numSquares(self, n: int) -> int:
    #     length = int(math.sqrt(n))
    #     dp = [[None] * (length + 1) for _ in range(n + 1)]

    #     # ini
    #     for k in range(length + 1):
    #         dp[0][k] = 0
    #     for i in range(n + 1):
    #         dp[i][1] = i

    #     for i in range(1, n + 1):
    #         for k in range(1, length + 1):
    #             if k > 1:
    #                 max_element_count = i // (k**2)
    #                 candidate = []
    #                 for m in range(max_element_count + 1):
    #                     candidate.append(m + dp[i - m * (k**2)][k - 1])
    #                 dp[i][k] = min(candidate)
    #     return dp[n][length]

    def numSquares(self, n: int) -> int:
        dp = [i for i in range(n + 1)]
        
        # 预计算平方数列表，减少重复计算
        squares = [i*i for i in range(1, int(n**0.5) + 1)]
        
        for i in range(1, n + 1):
            for square in squares:
                if i < square:
                    break
                # 状态转移：当前数 i 可以由 (i - square) 再加上一个 square 组成
                if dp[i - square] + 1 < dp[i]:
                    dp[i] = dp[i - square] + 1
        return dp[n]


# @lc code=end
