#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        nums_length = len(nums)
        # recursion ends
        if nums_length == 1:
            return nums[0]

        divide_stamp = nums_length // 2
        max_sum = max(
            self.maxSubArray(nums=nums[0:divide_stamp]),
            self.maxSubArray(nums=nums[divide_stamp:]),
        )

        # calculate from the divide stamp
        # calculate the left max sum
        max_left_sum = nums[divide_stamp-1]
        current_left_sum = 0
        for i in range(divide_stamp - 1, -1, -1):
            current_left_sum += nums[i]
            max_left_sum = max(current_left_sum, max_left_sum)

        max_right_sum = nums[divide_stamp]
        current_right_sum = 0
        for i in range(divide_stamp, nums_length, 1):
            current_right_sum += nums[i]
            max_right_sum = max(current_right_sum, max_right_sum)

        max_sum = max(max_sum, max_left_sum + max_right_sum)

        return max_sum


# @lc code=end
