#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#


# @lc code=start
# time complexity O(n^2)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # define dp[i][j] for judging s[i..j+1] is palindromic
        N = len(s)
        max_length = 1
        max_index = 0
        if N == 1:
            return s
        dp = [[False] * N for _ in range(N)]

        for i in range(N):
            dp[i][i] = True
        for i in range(N - 1):
            dp[i][i + 1] = s[i] == s[i + 1]
            if dp[i][i + 1]:
                max_length = 2
                max_index = i

        for length in range(3, N + 1):
            for begin_index in range(0, N - length + 1):
                # calculate [begin_index..begin_index + length]
                dp[begin_index][begin_index + length - 1] = dp[begin_index + 1][
                    begin_index + length - 2
                ] and (s[begin_index] == s[begin_index + length - 1])
                if dp[begin_index][begin_index + length - 1]:
                    max_length = length
                    max_index = begin_index
        return s[max_index : max_index + max_length]


# @lc code=end
