#
# @lc app=leetcode id=464 lang=python3
#
# [464] Can I Win
#


# @lc code=start
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        sum_all = (1 + maxChoosableInteger) * maxChoosableInteger // 2
        if sum_all < desiredTotal:
            return False

        if desiredTotal <= 0:
            return True

        memo = {}

        def dfs(current_total, mask):
            if mask in memo:
                return memo[mask]

            for i in range(maxChoosableInteger):
                # 检查第 i+1 个数字是否已被使用 (通过位运算)
                # (1 << i) 表示第 i+1 个数字的位掩码
                if not (mask & (1 << i)):
                    # 如果当前选了这个数之后能达到目标值，或者对手在下一个状态必输
                    # 那么当前玩家就赢了
                    if current_total + (i + 1) >= desiredTotal or not dfs(
                        current_total + (i + 1), mask | (1 << i)
                    ):
                        memo[mask] = True
                        return True

            # 如果所有数字选完都无法让对手必输，则当前玩家必输
            memo[mask] = False
            return False

        # 从初始状态开始：累计和为 0，掩码为 0（无数字被用过）
        return dfs(0, 0)


# @lc code=end
