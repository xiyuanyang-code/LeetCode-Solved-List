#
# @lc app=leetcode id=282 lang=python3
#
# [282] Expression Add Operators
#
from typing import List


# @lc code=start
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        length = len(num)
        res = []

        def recursive_splitting(index, current_expression, current_value, prev_element):
            if index == length:
                # finish scanning
                if current_value == target:
                    res.append(current_expression)
                    return

            for i in range(index, length):
                # do splitting!
                split_str = num[index : i + 1]

                # return invalid splitting
                if len(split_str) > 1 and split_str[0] == "0":
                    break

                # do operations
                try:
                    current_num = int(split_str)
                except Exception as e:
                    continue

                if index == 0:
                    recursive_splitting(
                        i + 1,
                        current_expression=split_str,
                        current_value=current_num,
                        prev_element=current_num,
                    )
                else:
                    # +
                    recursive_splitting(
                        i + 1,
                        current_expression=current_expression + "+" + split_str,
                        current_value=current_value + current_num,
                        prev_element=current_num,
                    )

                    # -
                    recursive_splitting(
                        i + 1,
                        current_expression=current_expression + "-" + split_str,
                        current_value=current_value - current_num,
                        prev_element=-current_num,
                    )

                    # *
                    recursive_splitting(
                        i + 1,
                        current_expression=current_expression + "*" + split_str,
                        current_value=(current_value - prev_element)
                        + prev_element * current_num,
                        prev_element=current_num * prev_element,
                    )

        recursive_splitting(0, "", 0, 0)
        return res


# @lc code=end
