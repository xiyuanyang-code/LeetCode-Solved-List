#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#
from typing import List


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        length = len(prices)
        dp = [None] * length
        dp[length - 1] = 0
        for i in range(length - 2, -1, -1):
            # if i choose to buy stocks at current date
            # choose the day to sell the stock
            candidates = []
            for j in range(i + 1, length):
                # we choose the sell the stock at the day of j
                current_income = prices[j] - prices[i]
                # we can choose to buy stocks at the end of the day j+2
                if j + 2 >= length:
                    future_income = 0
                else:
                    future_income = dp[j + 2]
                candidates.append(current_income + future_income)
            income = max(candidates) if candidates else 0
            # else just like tomorrow
            dp[i] = max(income, dp[i + 1])
        return dp[0]


# @lc code=end
