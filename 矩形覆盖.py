__author__ = 'luoyuedong'
__date__ = '2018/4/19 10:24'

# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        res = [0,1,2]
        while len(res)<=number:
            res.append(res[-1]+res[-2])
        return res[number]
