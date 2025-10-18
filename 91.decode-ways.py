#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#


# @lc code=start
class Solution:
    def is_valid(self, s: str) -> bool:
        if len(s) > 2:
            return False
        if s[0] != "1" and s[0] != "2":
            return False
        if int(s) > 26:
            return False
        return True

    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        d = [0] * (len(s))
        d[0] = 1 if s[0] != "0" else 0

        for i in range(1, len(s)):
            if s[i] != "0":
                d[i] += d[i - 1]
            if self.is_valid(s[i - 1 : i + 1]) and i - 2 >= 0:
                d[i] += d[i - 2]
            elif i == 1 and self.is_valid(s[i - 1 : i + 1]):
                d[i] += 1

        return int(d[len(s) - 1])


# @lc code=end
