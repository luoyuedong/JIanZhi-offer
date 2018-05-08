__author__ = 'luoyuedong'
__date__ = '2018/5/5 13:34'

# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        try :
            p = float(s)
            return True
        except:
            return False