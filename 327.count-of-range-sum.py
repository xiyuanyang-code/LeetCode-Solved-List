#
# @lc app=leetcode id=327 lang=python3
#
# [327] Count of Range Sum
#

from typing import List


# @lc code=start
# class Solution:
#     def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
#         if len(nums) == 0:
#             return 0
#         if len(nums) == 1:
#             return 1 if (lower <= nums[0] and nums[0] <= upper) else 0
        
#         # count the prefix sum
#         # * 注意 可以利用前缀和的 trick 来优化这个过程
#         prefix_sum = [0] * len(nums) + 1
#         for i in range(1, len(prefix_sum) + 1):
#             prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]

#         mid = len(nums) // 2
#         left_range_sum = self.countRangeSum(nums[:mid], lower, upper)
#         right_range_sum = self.countRangeSum(nums[mid:], lower, upper)

#         mid_count = 0
#         for i in range(mid - 1, -1, -1):
#             sum_res = sum(nums[i:mid])
#             for j in range(mid, len(nums)):
#                 sum_res += nums[j]
#                 if lower <= sum_res and sum_res <= upper:
#                     mid_count += 1
#         return left_range_sum + right_range_sum + mid_count

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        s = [0]
        for x in nums:
            s.append(s[-1] + x)
            
        def merge_sort(lo, hi):
            if hi - lo <= 1:
                return 0
            
            mid = (lo + hi) // 2
            # 递归计算左右两部分
            count = merge_sort(lo, mid) + merge_sort(mid, hi)
            
            # 2. 核心：在合并前统计跨越左右的合法对
            # 此时 s[lo:mid] 和 s[mid:hi] 已经由于递归内部的排序变为了有序
            i = j = mid
            for left_val in s[lo:mid]:
                # 寻找右侧数组中第一个满足 s[j] - left_val >= lower 的位置
                while i < hi and s[i] - left_val < lower:
                    i += 1
                # 寻找右侧数组中第一个满足 s[j] - left_val > upper 的位置
                while j < hi and s[j] - left_val <= upper:
                    j += 1
                count += (j - i)
            
            # 3. 标准归并排序的合并步骤
            s[lo:hi] = sorted(s[lo:hi])
            return count

        return merge_sort(0, len(s))


# @lc code=end
