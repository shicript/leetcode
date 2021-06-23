'''
Descripttion: 
version: 
Author: Shicript
Date: 2021-06-23 11:55:39
LastEditors: Shicript
LastEditTime: 2021-06-23 11:56:02
'''
#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        if len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]

        s_cp = s[0] * len(s)
        if s_cp == s:
            return s

        longest_s = ""
        max_len = 0

        for i, char in enumerate(s):
            pre_s = s[:i]
            last_s = s[i+1:]

            if pre_s and last_s:
                pre_sentence, last_sentence = Solution.get_pre_and_lst(
                    pre_s, last_s)
                sent = pre_sentence + char + last_sentence
                if len(sent) > max_len:
                    longest_s = sent
                    max_len = len(sent)

            pre_s_append = pre_s + char
            if pre_s_append and last_s:
                pre_sentence, last_sentence = Solution.get_pre_and_lst(
                    pre_s_append, last_s)
                sent = pre_sentence + last_sentence
                if len(sent) > max_len:
                    longest_s = sent
                    max_len = len(sent)

        if max_len == 0:
            return s[0]
        return longest_s

    @staticmethod
    def get_pre_and_lst(pre_s, last_s):
        pre_s_reversed = list(reversed(pre_s))
        sim_num = Solution.findMaxLength(pre_s_reversed, last_s)

        if sim_num == 0:
            return "", ""

        pre_sentence = pre_s[-sim_num:]
        last_sentence = last_s[:sim_num]

        return pre_sentence, last_sentence

    @staticmethod
    def findMaxLength(s1, s2):
        max_len = 0
        for i in range(min(len(s1), len(s2))):
            if s1[i] == s2[i]:
                max_len += 1
            else:
                break
        return max_len


# @lc code=end

