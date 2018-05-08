__author__ = 'luoyuedong'
__date__ = '2018/5/5 13:58'

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# class Solution:
#     def deleteDuplication(self, pHead):
#         if pHead is None or pHead.next is None:
#             return pHead
#         head1 = pHead.next
#         if head1.val != pHead.val:
#             pHead.next = self.deleteDuplication(pHead.next)
#         else:
#             while pHead.val == head1.val and head1.next is not None:
#                 head1 = head1.next
#             if head1.val != pHead.val:
#                 pHead = self.deleteDuplication(head1)
#             else:
#                 return None
#         return pHead

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteDuplication(self, pHead):

        first = ListNode(-1)
        first.next = pHead
        last = first
        p = pHead
        while(p is not None and p.next is not None):
            if(p.val == p.next.val):
                val = p.val
                while(p is not None and p.val==val):
                    p = p.next
                last.next = p
            else:
                last = p
                p = p.next
        return first.next