__author__ = 'luoyuedong'
__date__ = '2018/5/5 9:52'

# -*- coding:utf-8 -*-
class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n<1:
            return -1
        con = range(n)
        final = -1
        start = 0
        while con:
            start = (start+m-1)%n
            n = n-1
            final = con.pop(start)
        return final