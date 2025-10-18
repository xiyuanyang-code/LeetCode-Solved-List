#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
from typing import List

class Solution:
    def find_median_of_small_array(self, arr: List[int]) -> int:
        # O(1) for constant length arrays
        arr.sort()
        return arr[len(arr) // 2]
    
    def select_pivot(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 5:
            return self.find_median_of_small_array(arr)
        
        # splitting into sub-lists
        sublists = [arr[i : i + 5] for i in range(0, n, 5)]
        medians = [self.find_median_of_small_array(sublist) for sublist in sublists]
        
        # ! very important recursion!
        # That is the T(n/5) part
        return self.findKthSmallest(medians, len(medians) // 2 + 1) # 找第 k 小的元素，k 从 1 开始

    def findKthSmallest(self, arr: List[int], k: int) -> int:
        n = len(arr)
        if n == 1:
            return arr[0]
        
        pivot = self.select_pivot(arr)
        
        # do partition based on selected pivot
        less = [x for x in arr if x < pivot]
        equal = [x for x in arr if x == pivot]
        greater = [x for x in arr if x > pivot]
        
        len_less = len(less)
        len_equal = len(equal)
        
        # the core recursion part remains unchanged
        if k <= len_less:
            return self.findKthSmallest(less, k)
        elif k <= len_less + len_equal:
            return pivot
        else:
            new_k = k - len_less - len_equal
            return self.findKthSmallest(greater, new_k)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        k_smallest = n - k + 1 
        return self.findKthSmallest(nums, k_smallest)

# @lc code=end
