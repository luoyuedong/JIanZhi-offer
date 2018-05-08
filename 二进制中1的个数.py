__author__ = 'luoyuedong'
__date__ = '2018/4/19 10:34'

# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        count = 0
        if n<0:
            n = n & 0xffffffff
        while(n):
            n = n & (n-1)
            count += 1
        return count

    def NumberOf2(self, n):
        return bin(n).count("1") if n>=0 else bin(2**32+n).count("1")