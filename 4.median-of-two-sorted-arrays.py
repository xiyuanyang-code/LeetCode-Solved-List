#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        total_len = m + n

        if total_len % 2 == 1:
            k = total_len // 2 + 1
            return self._findKth(nums1, 0, nums2, 0, k)
        else:
            k1 = total_len // 2
            k2 = total_len // 2 + 1
            median1 = self._findKth(nums1, 0, nums2, 0, k1)
            median2 = self._findKth(nums1, 0, nums2, 0, k2)
            return (median1 + median2) / 2.0

    def _findKth(self, nums1: list[int], i: int, nums2: list[int], j: int, k: int) -> int:
        # i and j means the starting index
        # len1 and len2 are the length of the sub arrays
        len1 = len(nums1) - i
        len2 = len(nums2) - j

        if len1 == 0:
            return nums2[j + k - 1]
        if len2 == 0:
            return nums1[i + k - 1]

        if k == 1:
            return min(nums1[i], nums2[j])

        half_k = k // 2
        
        # 确定要比较的元素索引
        idx1 = i + min(len1, half_k) - 1
        idx2 = j + min(len2, half_k) - 1
        val1 = nums1[idx1]
        val2 = nums2[idx2]

        if val1 <= val2:
            # 排除 nums1 中的 [i, idx1] 部分
            new_k = k - (idx1 - i + 1)
            return self._findKth(nums1, idx1 + 1, nums2, j, new_k)
        else: # val2 < val1
            new_k = k - (idx2 - j + 1)
            return self._findKth(nums1, i, nums2, idx2 + 1, new_k)

# @lc code=end
