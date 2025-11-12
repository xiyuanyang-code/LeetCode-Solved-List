#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        length_nums = len(nums)
        if length_nums == 1:
            return nums[0]
        max_end = [None] * length_nums
        min_end = [None] * length_nums
        max_end[0] = nums[0]
        min_end[0] = nums[0]
        for i in range(1, length_nums):
            if nums[i] > 0:
                max_end[i] = max(max_end[i-1] * nums[i], nums[i])
                min_end[i] = min(min_end[i-1] * nums[i], nums[i])
            elif nums[i] == 0:
                max_end[i] = 0
                min_end[i] = 0
            else:
                max_end[i] = max(min_end[i-1] * nums[i], nums[i])
                min_end[i] = min(max_end[i-1] * nums[i], nums[i])
        return max(max_end)

    def maxProduct_old(self, nums: List[int]) -> int:
        length_nums = len(nums)
        if length_nums == 1:
            return nums[0]
        dp = [None] * (length_nums)
        dp[0] = nums[0]
        for i in range(1, length_nums):
            # find the current maximum
            current_maximum = nums[i]
            current_value = nums[i]
            for j in range(i - 1, -1, -1):
                current_value *= nums[j]
                current_maximum = max(current_maximum, current_value)
            dp[i] = max(dp[i - 1], current_maximum)
        return dp[length_nums - 1]


# @lc code=end
