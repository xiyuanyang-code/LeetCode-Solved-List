#
# @lc app=leetcode id=474 lang=python3
#
# [474] Ones and Zeroes
#

from typing import List


# @lc code=start
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # dp[i][m][n]
        dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(len(strs) + 1)]
        for i in range(1, len(strs) + 1):
            for m_cur in range(0, m + 1):
                for n_cur in range(0, n + 1):
                    m_count = strs[i - 1].count("0")
                    n_count = strs[i - 1].count("1")
                    if m_count > m_cur or n_count > n_cur:
                        # forbid this
                        dp[i][m_cur][n_cur] = max(
                            dp[i][m_cur][n_cur], dp[i - 1][m_cur][n_cur]
                        )
                    else:
                        dp[i][m_cur][n_cur] = max(
                            dp[i][m_cur][n_cur],
                            dp[i - 1][m_cur][n_cur],
                            dp[i - 1][m_cur - m_count][n_cur - n_count] + 1,
                        )
        return dp[len(strs)][m][n]


# @lc code=end
