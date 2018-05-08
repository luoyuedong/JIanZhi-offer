__author__ = 'luoyuedong'
__date__ = '2018/5/5 9:13'

# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        length = len(s)
        if length == 0:
            return ""
        n = n%length
        a = s[n:length]
        b = s[:n]
        return a+b