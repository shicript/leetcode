'''
Descripttion: 
version: 
Author: Shicript
Date: 2021-06-23 11:56:44
LastEditors: Shicript
LastEditTime: 2021-06-23 11:56:59
'''
#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x < 10:
            return True
        if x % 10 == 0:
            return False

        def get_num_list(x: int) -> list:
            res_num_list = []
            while int(x / 10) > 0:
                res_num_list.append(x % 10)
                x = int(x / 10)
            res_num_list.append(x)
            return res_num_list

        num_list = get_num_list(x)
        num_len = len(num_list)

        if num_len % 2 == 0:
            pre_list = num_list[:int(num_len/2)]
            las_list = num_list[int(num_len/2):]
            las_list_reversed = list(reversed(las_list))
            if pre_list == las_list_reversed:
                return True
            return False
        else:
            center_num_index = int((num_len - 1)/2)

            pre_list = num_list[:center_num_index]
            las_list = num_list[center_num_index+1:]
            las_list_reversed = list(reversed(las_list))
            if pre_list == las_list_reversed:
                return True
            return False


# @lc code=end

