#
# @lc app=leetcode id=315 lang=python3
#
# [315] Count of Smaller Numbers After Self
#
from typing import List


# @lc code=start
from typing import List

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        self.res = [0] * n
        # 将数值和它的原始索引绑定，形如 [(v1, 0), (v2, 1), ...]
        # 这样排序后我们依然知道某个数原来的位置在哪里
        indexed_nums = list(enumerate(nums))
        self.merge_sort(indexed_nums)
        return self.res

    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])
        
        return self.merge(left, right)

    def merge(self, left, right):
        merged = []
        i = 0  # 左侧数组指针
        j = 0  # 右侧数组指针
        
        # 合并阶段
        while i < len(left) and j < len(right):
            # 如果左边的数大于右边的数
            # 注意：left[i][1] 是该元素在原始 nums 中的索引
            if left[i][1] > right[j][1]:
                # 关键：当右边的元素被放入合并数组时，
                # 它意味着对于【左边剩余的所有元素】，都发现了一个比它们小的右侧元素。
                # 但更简单的做法是：当左边元素落位时，统计它跳过了多少个右边元素。
                merged.append(right[j])
                j += 1
            else:
                # 左边元素落位，此时 j 的数值就是右边比它小的元素个数
                self.res[left[i][0]] += j
                merged.append(left[i])
                i += 1
        
        # 处理剩余元素
        while i < len(left):
            self.res[left[i][0]] += j
            merged.append(left[i])
            i += 1
        
        while j < len(right):
            merged.append(right[j])
            j += 1
            
        return merged

# @lc code=end
