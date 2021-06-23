'''
Descripttion: 
version: 
Author: Shicript
Date: 2021-06-23 11:55:02
LastEditors: Shicript
LastEditTime: 2021-06-23 11:55:30
'''
#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums = sorted(nums)

        nums_len = len(nums)

        if nums_len % 2 == 0:
            half_len = int(nums_len / 2)
            return (nums[half_len - 1] + nums[half_len]) / 2
        elif nums_len % 2 == 1:
            return nums[int((nums_len-1)/2)]
# @lc code=end

