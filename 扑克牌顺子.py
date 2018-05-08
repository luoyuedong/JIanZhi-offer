__author__ = 'luoyuedong'
__date__ = '2018/5/5 9:38'

# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        numbers.sort()
        if len(numbers)!=5:
            return False
        zero = numbers.count(0)
        for i,v in enumerate(numbers[:-1]):
            if v!=0:
                if numbers[i+1]==v:return False
                zero = zero - (numbers[i+1]-v) + 1
                if zero<0:
                    return False
        return  True
