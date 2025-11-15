#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        def rob_linear(l: int, r: int) -> int:
            # dp[i] = 在前 i 个房子中能偷到的最大金额
            prev2 = prev1 = 0
            for i in range(l, r + 1):
                cur = max(prev1, prev2 + nums[i])
                prev2, prev1 = prev1, cur
            return prev1

        opt1 = rob_linear(0, n - 2)
        opt2 = rob_linear(1, n - 1)

        return max(opt1, opt2)
# @lc code=end

