#
# @lc app=leetcode id=939 lang=python3
#
# [939] Minimum Area Rectangle
#
from typing import List
# @lc code=start
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        # create a hash set and store all the points into it
        points_hash = set()
        min_area = 1e10
        for point in points:
            points_hash.add((point[0], point[1]))
            
        for point_1 in points:
            for point_2 in points:
                x_1, y_1 = point_1
                x_2, y_2 = point_2
                if (x_1 == x_2 or y_1 == y_2):
                    continue
                if (x_1, y_2) in points_hash and (x_2, y_1) in points_hash:
                    # the value for the rectangle
                    min_area = min(min_area, abs((x_1 - x_2)*(y_1 - y_2)))
        return min_area
        
# @lc code=end

