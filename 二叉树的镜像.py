__author__ = 'luoyuedong'
__date__ = '2018/5/6 19:42'

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        if root==None:
            return
        tmp = root.left
        root.left = root.right
        root.right = tmp
        self.Mirror(root.left)
        self.Mirror(root.right)