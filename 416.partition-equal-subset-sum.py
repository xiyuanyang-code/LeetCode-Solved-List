#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#

# @lc code=start
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        target_sum = int(total_sum / 2)
        # we need to find a sub string which matches the target sum: 0/1 package problems!
        dp = [[False] * (len(nums) + 1) for _ in range(target_sum + 1)]
        dp[0][0] = True
        for i in range(target_sum + 1):
            for j in range(1, len(nums) + 1):
                if i == 0:
                    dp[i][j] = True
                    continue
                if i - nums[j - 1] >= 0:
                    dp[i][j] = dp[i - nums[j - 1]][j - 1] or dp[i][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]
        return dp[target_sum][len(nums)]


# @lc code=end
