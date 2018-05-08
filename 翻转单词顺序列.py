__author__ = 'luoyuedong'
__date__ = '2018/5/5 9:29'

# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        return " ".join(s.split(" ")[::-1])