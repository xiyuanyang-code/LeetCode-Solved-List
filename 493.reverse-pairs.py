#
# @lc app=leetcode id=493 lang=python3
#
# [493] Reverse Pairs
#

from typing import List


# @lc code=start
from typing import List

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def solve(lst):
            if len(lst) <= 1:
                return 0, lst
            
            mid = len(lst) // 2
            count_l, left = solve(lst[:mid])
            count_r, right = solve(lst[mid:])
            
            mid_count = 0
            j = 0
            for i in range(len(left)):
                while j < len(right) and left[i] > 2 * right[j]:
                    j += 1
                mid_count += j
            
            merged = []
            p1, p2 = 0, 0
            while p1 < len(left) and p2 < len(right):
                if left[p1] <= right[p2]:
                    merged.append(left[p1])
                    p1 += 1
                else:
                    merged.append(right[p2])
                    p2 += 1
            merged.extend(left[p1:])
            merged.extend(right[p2:])
            
            return count_l + count_r + mid_count, merged

        total_count, sorted_nums = solve(nums)
        return total_count

# @lc code=end
