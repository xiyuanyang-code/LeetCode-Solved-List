#
# @lc app=leetcode id=264 lang=python3
#
# [264] Ugly Number II
#


# @lc code=start
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0] * n
        dp[0] = 1
        
        # p2, p3, p5 分别代表丑数序列中等待乘以 2, 3, 5 的位置
        p2 = p3 = p5 = 0
        
        for i in range(1, n):
            # 找到三个序列中的最小值，作为下一个丑数
            next_2 = dp[p2] * 2
            next_3 = dp[p3] * 3
            next_5 = dp[p5] * 5
            
            curr_ugly = min(next_2, next_3, next_5)
            dp[i] = curr_ugly
            
            if curr_ugly == next_2:
                p2 += 1
            if curr_ugly == next_3:
                p3 += 1
            if curr_ugly == next_5:
                p5 += 1
                
        return dp[n - 1]


# @lc code=end
