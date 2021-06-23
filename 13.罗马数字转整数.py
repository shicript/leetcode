'''
Descripttion: 
version: 
Author: Shicript
Date: 2021-06-22 20:21:07
LastEditors: Shicript
LastEditTime: 2021-06-23 10:19:51
'''
#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#
# @lc code=start
from functools import reduce


class Solution:
    def romanToInt(self, s: str) -> int:
        s_reversed = list(reversed(s))
        node = RomaNode(s_reversed[0])
        s_reversed = [node] + s_reversed[1:]
        node = reduce(self.build_node, s_reversed)
        return self.get_node_value(node)

    @staticmethod
    def get_node_value(node):
        left_char_dict = {"I": {"V": 4, "X": 9}, "X": {
            "L": 40, "C": 90}, "C": {"D": 400, "M": 900}}
        char_num_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        res_number = 0
        end_with_left = False
        while node.next:
            value1 = node.value
            node = node.next
            value2 = node.value
            if value1 in left_char_dict.keys():
                if value2 in left_char_dict[value1].keys():
                    res_number += left_char_dict[value1][value2]
                    if node.next:
                        node = node.next
                    else:
                        end_with_left = True
                    continue
            res_number += char_num_dict[value1]
            end_with_left = False
        if not end_with_left:
            res_number += char_num_dict[node.value]
        return res_number

    @staticmethod
    def build_node(node1, char2):
        node2 = RomaNode(char2)
        node2.next = node1
        return node2


class RomaNode:
    def __init__(self, x):
        self.value = x
        self.next = None

# @lc code=end

