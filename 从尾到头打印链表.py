__author__ = 'luoyuedong'
__date__ = '2018/4/17 23:09'

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        arr = []
        if listNode is None:
            return arr
        while(listNode.next is not None):
            arr.append(listNode.val)
            listNode = listNode.next
        arr.append(listNode.val)
        arr.reverse()
        return arr
