#
# @lc app=leetcode id=241 lang=python3
#
# [241] Different Ways to Add Parentheses
#

from typing import List
import itertools


# @lc code=start
class Solution:
    def merge(self, operation: str, result_product) -> List[int]:
        if operation == "+":
            return [left + right for (left, right) in result_product]
        elif operation == "-":
            return [left - right for (left, right) in result_product]
        else:
            return [left * right for (left, right) in result_product]

    def diffWaysToCompute(self, expression: str) -> List[int]:
        final_result = []
        # 思路：首先选择一个符号，这个符号作为运算树的最后一个操作符
        # 递归到左边的 expression 和 右边的 expression
        # 递归的终点：当 expression 只剩下一个数的时候，就是这个数本身
        # 合并的过程：做一个笛卡尔积

        length_exp = len(expression)
        # check whether the expression is a pure number
        if (
            ("+" not in expression)
            and ("-" not in expression)
            and ("*" not in expression)
        ):
            # the result is itself
            return [int(expression)]
        # splitting for expression
        for index in range(1, length_exp):
            operations = str(expression[index]).strip()
            if operations == "+" or operations == "-" or operations == "*":
                left_exp = expression[:index]
                right_exp = expression[(index + 1) :]

                # recursively
                left_results = self.diffWaysToCompute(left_exp)
                right_results = self.diffWaysToCompute(right_exp)

                # merge the results
                result_product = list(itertools.product(left_results, right_results))
                final_result.extend(
                    self.merge(operation=operations, result_product=result_product)
                )

        return final_result


# @lc code=end
