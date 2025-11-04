#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#

# @lc code=start
# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self.generateTreehelper(1, n)

    def generateTreehelper(self, start: int, end: int):
        # the node is from start to end (both included
        if start > end:
            return [None]
        elif start == end:
            return [TreeNode(val=start)]
        else:
            # start < end
            results = []
            for root_node in range(start, end+1):
                # append left sub_tree and right subtree
                left_subtree_list = self.generateTreehelper(start=start, end=root_node-1)
                right_subtree_list = self.generateTreehelper(start=root_node+1, end=end)
                for left_subtree in left_subtree_list:
                    for right_subtree in right_subtree_list:
                        results.append(TreeNode(val=root_node, left=left_subtree,right=right_subtree))
            return results
                


# @lc code=end
