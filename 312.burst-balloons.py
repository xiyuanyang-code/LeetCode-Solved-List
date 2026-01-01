#
# @lc app=leetcode id=312 lang=python3
#
# [312] Burst Balloons
#
from typing import List


# @lc code=start
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        memo = {}
        nums = [1] + nums + [1]

        def solve(left: int, right: int):
            if (left, right) in memo:
                return memo[(left, right)]
            if left+1 >= right:
                return 0
            if right - left == 2:
                memo[(left, right)] = nums[left] * nums[left + 1] * nums[left + 2]
                return memo[(left, right)]

            # 求解 (i,j) 的子问题
            # * 注意这里是开区间！
            sum = 0
            for pivot in range(left + 1, right):
                current_sum = 0
                current_sum += solve(left, pivot)
                current_sum += solve(pivot, right)
                current_sum += nums[pivot] * nums[left] * nums[right]
                sum = max(sum, current_sum)
            memo[(left, right)] = sum
            return sum

        return solve(0, len(nums) - 1)


# @lc code=end
