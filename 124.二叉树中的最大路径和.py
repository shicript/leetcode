'''
Descripttion: 
version: 
Author: Shicript
Date: 2021-07-12 15:17:00
LastEditors: Shicript
LastEditTime: 2021-07-12 16:17:24
'''
#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def __init__(self):
        self.res = -1000
    
    def maxPathSum(self, root):
        self.maxPathSum_1(root)
        return self.res

    def maxPathSum_1(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        left = max(self.maxPathSum_1(root.left), 0)
        right = max(self.maxPathSum_1(root.right), 0)
        self.res = max(self.res, left+right+root.val)
        return max(left+root.val, right+root.val)
# @lc code=end

if __name__=='__main__':
    sl = Solution()
    tn_left = TreeNode(val=2)
    tn_right = TreeNode(val=3)
    tn = TreeNode(val=1, left=tn_left, right=tn_right)
    res = sl.maxPathSum(root=tn)
    print(res)

