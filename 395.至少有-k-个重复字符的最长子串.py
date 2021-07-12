'''
Descripttion: 
version: 
Author: Shicript
Date: 2021-07-12 16:28:25
LastEditors: Shicript
LastEditTime: 2021-07-12 17:05:42
'''
#
# @lc app=leetcode.cn id=395 lang=python3
#
# [395] 至少有 K 个重复字符的最长子串
#

# @lc code=start
from typing import Set


class Solution:
    def __init__(self):
        self.max_len = 0

    def longestSubstring(self, s, k):
        self.longestSub(s, k)
        return self.max_len


    def longestSub(self, s: str, k: int) -> int:
        char_dict = {}
        for c in s:
            if c in char_dict.keys():
                char_dict[c] = char_dict[c]+1
            else:
                char_dict[c] = 1
        
        remove_char_list = set()
        for c in s:
            if char_dict[c] < k:
                remove_char_list.add(c)

        if len(remove_char_list) == 0:
            self.max_len = max(len(s), self.max_len)
            return self.max_len
        
        str_list = [s_sub for s_sub in s.split(remove_char_list.pop()) if s_sub != '']
        for str_piece in str_list:
            self.longestSub(str_piece, k)

        
        
# @lc code=end

if __name__=='__main__':
    sl = Solution()
    str_input = "aaabb"
    print(sl.longestSubstring(str_input, 3))

