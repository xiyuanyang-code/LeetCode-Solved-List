#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#

from typing import List


# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        # starting point
        i = 0
        j = n - 1

        # 如果要找更小的数字，往左边走
        # 如果要找更大的数字，往下边走
        # 跳出循环的条件：坐标超出范围

        while True:
            # check boundaries:
            if i < 0 or i >= m or j < 0 or j >= n:
                break
            current_num = matrix[i][j]
            if current_num == target:
                return True
            elif current_num < target:
                # choose bigger numbers
                i += 1
            else:
                # choose smaller numbers
                j -= 1
        return False


# @lc code=end
