'''
Descripttion: 
version: 
Author: Shicript
Date: 2021-06-23 11:51:11
LastEditors: Shicript
LastEditTime: 2021-06-23 11:54:00
'''
#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_list, l2_list = [], []
        while l1.next:
            l1_list.append(l1.val)
            l1 = l1.next

        while l2.next:
            l2_list.append(l2.val)
            l2 = l2.next

        l1_list.append(l1.val)
        l2_list.append(l2.val)

        l1_reversed = list(reversed(l1_list))
        l2_reversed = list(reversed(l2_list))

        l1_reverse_num = reduce(lambda x, y: 10*x+y, l1_reversed)
        l2_reverse_num = reduce(lambda x, y: 10*x+y, l2_reversed)

        reverse_sum_str = str(l1_reverse_num + l2_reverse_num)

        result = ListNode(int(reverse_sum_str[0]))

        for index, num in enumerate(reverse_sum_str):
            if index == 0:
                continue
            tmp = ListNode(int(num))
            tmp.next = result
            result = tmp

        return result



# @lc code=end

