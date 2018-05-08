__author__ = 'luoyuedong'
__date__ = '2018/4/19 10:05'

# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        a = 1
        b = 1
        while(number):
            b = a+b
            a = b-a
            number -= 1
        return a