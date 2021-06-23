'''
Descripttion: 
version: 
Author: Shicript
Date: 2021-06-23 11:54:18
LastEditors: Shicript
LastEditTime: 2021-06-23 11:54:51
'''
#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start

import copy


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        candicate_nums = {}
        for idx, num in enumerate(nums):
            # if num > target:
            #     continue
            candicate_nums.setdefault(idx, num)

        backup = copy.deepcopy(candicate_nums)

        for idx, num in candicate_nums.items():
            backup.pop(idx)
            dif = target - num
            if dif == 0 and num != 0:
                # return [idx]
                continue
            else:
                if dif in backup.values():
                    return [idx, self.get_key(candicate_nums, dif, idx)]
                else:
                    continue

    def get_key(self, dict, v, i):
        for key, value in dict.items():
            if key == i:
                continue
            if v == value:
                return key
# @lc code=end

