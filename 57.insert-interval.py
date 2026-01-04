#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#
from typing import List

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        return self.merge(intervals)

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort the array based on the first index
        intervals = sorted(intervals,key=lambda x: x[0])
        i = 0
        merged_list = []
        while i < len(intervals):
            j = i
            current_right_bound = intervals[j][1]
            while j < len(intervals) and intervals[j][0] <= current_right_bound:
                # update current right bound
                current_right_bound = max(current_right_bound, intervals[j][1])
                j += 1

            left_bound = intervals[i][0]
            right_bound = current_right_bound
            merged_list.append([left_bound, right_bound])
            i = j

        return merged_list
        
# @lc code=end

