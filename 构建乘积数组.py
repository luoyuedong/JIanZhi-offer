__author__ = 'luoyuedong'
__date__ = '2018/5/5 13:10'

# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        head = [1]
        tail = [1]
        for i in range(len(A)-1):
            head.append(A[i]*head[i])
            tail.append(A[-i-1]*tail[i])
        return [head[j]*tail[-j-1] for j in range(len((head)))]