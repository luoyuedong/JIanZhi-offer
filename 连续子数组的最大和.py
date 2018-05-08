__author__ = 'luoyuedong'
__date__ = '2018/5/7 21:15'
# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        thisSum = 0
        maxSum = array[0]
        for i in range(len(array)):
            thisSum+=array[i]
            if thisSum>maxSum:
                maxSum = thisSum
            if(thisSum<0):
                thisSum = 0
        return maxSum