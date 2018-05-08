__author__ = 'luoyuedong'
__date__ = '2018/5/5 10:47'

# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        for i in range(numbers):
            if numbers.count(numbers[i])>1:
                return numbers[i]
        return ""