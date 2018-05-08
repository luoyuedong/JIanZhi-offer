__author__ = 'luoyuedong'
__date__ = '2018/5/4 21:53'

# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        n = tsum**0.5
        n = int(n)
        res = []
        for i in range(1,tsum/2+1):
            sumres = i
            for j in range(i+1,tsum/2+2):
                sumres+=j
                if sumres == tsum:
                    res.append(list(range(i,j+1)))
                    break
                elif sumres>tsum:
                    break
        return res