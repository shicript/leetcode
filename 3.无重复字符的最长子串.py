'''
@Descripttion:
@version:
@Author: Shicript
@Date: 2020-07-28 19:53:21
LastEditors: Shicript
LastEditTime: 2021-06-22 00:51:19
'''
#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        if len(s)==0:
            return 0
        if len(s)==1:
            return 1
        for i, v in enumerate(s):
            tmp = set()
            tmp.add(v)
            cur_len = 1
            for v2 in s[i+1:]:
                if v2 not in tmp:
                    tmp.add(v2)
                    cur_len += 1
                else:
                    max_len = cur_len if max_len < cur_len else max_len
                    break
            max_len = cur_len if max_len < cur_len else max_len
            cur_len = 0
        return max_len
        
# @lc code=end
