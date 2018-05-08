__author__ = 'luoyuedong'
__date__ = '2018/5/3 22:12'

# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        taglist = []
        for i in array:
            if array.count(i)==1 and i not in taglist:
                taglist.append(i)
        return taglist