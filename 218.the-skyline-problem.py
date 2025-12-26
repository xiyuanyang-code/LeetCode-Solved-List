#
# @lc app=leetcode id=218 lang=python3
#
# [218] The Skyline Problem
#

from typing import List


# @lc code=start
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        if len(buildings) == 1:
            return [
                [buildings[0][0], buildings[0][2]],
                [buildings[0][1], 0],
            ]
        length = len(buildings)
        pivot_index = length // 2
        left = self.getSkyline(buildings=buildings[:pivot_index])
        right = self.getSkyline(buildings=buildings[pivot_index:])

        # merge two skylines
        l_idx = 0
        r_idx = 0
        l_h = 0
        r_h = 0
        res = []

        while l_idx < len(left) and r_idx < len(right):
            if left[l_idx][0] < right[r_idx][0]:
                x, l_h = left[l_idx]
                l_idx += 1
            elif left[l_idx][0] > right[r_idx][0]:
                x, r_h = right[r_idx]
                r_idx += 1
            else: # x 相同的情况
                x, l_h = left[l_idx]
                r_h = right[r_idx][1]
                l_idx += 1
                r_idx += 1
            
            # 2. 当前天际线的高度是两者的最大值
            max_h = max(l_h, r_h)
            
            # 3. 如果高度变化了，才记录（去重）
            if not res or res[-1][1] != max_h:
                res.append([x, max_h])
                
        # 4. 把剩余的坐标点补齐
        res.extend(left[l_idx:])
        res.extend(right[r_idx:])
        return res




# @lc code=end
