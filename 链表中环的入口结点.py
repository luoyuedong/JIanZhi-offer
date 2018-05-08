__author__ = 'luoyuedong'
__date__ = '2018/5/5 13:43'

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        slowptr = pHead
        fastptr = pHead
        while slowptr.next!=None and fastptr.next.next!=None:
            slowptr = slowptr.next
            fastptr = fastptr.next.next
            if slowptr == fastptr:
                slow2 = pHead
                while slow2 != slowptr:
                    slow2 = slow2.next
                    slowptr =slowptr.next
                return slowptr