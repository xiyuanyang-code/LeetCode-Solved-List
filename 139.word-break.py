#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

from typing import List
# @lc code=start
class Solution:
    # time complexity O(n^2)
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        min_len = min(len(w) for w in wordDict)
        max_len = max(len(w) for w in wordDict)
        length = len(s)
        if length == 0:
            return True
        # define dp[i] means s[:i]
        dp = [False] * (length + 1)
        dp[0] = True
        for i in range(1, length+1):
            #* optimize for constant
            for j in range(max(0, i - max_len), i - min_len + 1):
                if s[j:i] in wordDict and dp[j]:
                    dp[i] = True
                    break
        return dp[length]
        
# @lc code=end

