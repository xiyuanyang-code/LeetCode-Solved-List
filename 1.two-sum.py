#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

from typing import List


# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 1:
            return None
        if len(nums) == 2:
            return [0, 1]

        if target % 2 == 0:
            half = target / 2
            ans = []
            for index, num in enumerate(nums):
                if num == half:
                    ans.append(index)
                    if len(ans) == 2:
                        return ans
            
        backup_list = set(nums)
        for i, num in enumerate(nums):
            another_piece = target - num
            if another_piece != num:
                if another_piece in nums:
                    break
        # we need to find another piece
        for j, another_num in enumerate(nums):
            if another_num == another_piece:
                break
        return [i, j]


# @lc code=end
