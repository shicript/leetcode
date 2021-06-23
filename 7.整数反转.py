'''
Descripttion: 
version: 
Author: Shicript
Date: 2021-06-23 11:56:13
LastEditors: Shicript
LastEditTime: 2021-06-23 11:56:38
'''
#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start


class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return x

        if x < 0:
            below_zero = True
        else:
            below_zero = False

        num_limit = (1 << 31) - 1
        num_limit_below = - (1 << 31)

        x = abs(x)
        x_str = str(x)
        x_str_reversed = reversed(x_str)

        num_list = []
        for char in x_str_reversed:
            if char == '0' and len(num_list) == 0:
                continue
            else:
                num_list.append(char)

        if below_zero:
            numb = -int(''.join(num_list))
            return numb if num_limit_below < numb < num_limit else 0
        numb = int(''.join(num_list))
        return numb if num_limit_below < numb < num_limit else 0
# @lc code=end

