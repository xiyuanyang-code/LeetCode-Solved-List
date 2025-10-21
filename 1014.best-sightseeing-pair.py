#
# @lc app=leetcode id=1014 lang=python3
#
# [1014] Best Sightseeing Pair
#
from typing import List


# @lc code=start
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        value_length = len(values)
        # where recursion ends
        if value_length == 2:
            return values[0] + values[1] - 1

        if value_length == 3:
            return max(
                (values[0] + values[1] - 1),
                (values[0] + values[2] - 2),
                (values[1] + values[2] - 1),
            )

        # for the value_length >= 4
        splitting_index = value_length // 2
        max_score_1 = self.maxScoreSightseeingPair(values=values[:splitting_index])
        max_score_2 = self.maxScoreSightseeingPair(values=values[splitting_index:])
        # calculate the max_value of v[i] + i, where 0 <= i <= split-1
        max_left = values[0]
        for i in range(splitting_index):
            max_left = max(values[i] + i, max_left)
        max_right = values[splitting_index] - splitting_index
        for j in range(splitting_index, value_length):
            max_right = max(values[j] - j, max_right)
        return max(max_score_1, max_score_2, (max_left + max_right))


# algorithms analysis
# The time complexity is O(n log n)
# T(n) = 2 T(n/2) + Theta(n)

# @lc code=end
