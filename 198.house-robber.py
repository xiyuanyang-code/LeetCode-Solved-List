#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        len_nums = len(nums)
        dp_have = [0] * len_nums
        dp_not_have = [0] * len_nums
        
        dp_have[0] = nums[0]
        dp_not_have[0] = 0
        if len_nums == 1:
            return max(dp_have[0], dp_not_have[0])
        
        dp_have[1] = nums[1]
        dp_not_have[1] = nums[0]
        if len_nums == 2:
            return max(dp_have[1], dp_not_have[1])
        
        for i in range(2, len_nums):
            dp_have[i] = nums[i] + max(dp_have[i-2], dp_not_have[i-2])
            dp_not_have[i] = max(dp_have[i-1], dp_not_have[i-1])
        
        return max(dp_not_have[len_nums-1], dp_have[len_nums-1])
        
# @lc code=end

