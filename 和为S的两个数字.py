__author__ = 'luoyuedong'
__date__ = '2018/5/5 9:01'

# -*- coding:utf-8 -*-
# class Solution:
#     def FindNumbersWithSum(self, array, tsum):
#         # write code here
#         n = len(array)
#         i = 0
#         j = n-1
#         res = []
#         while(i<j):
#             if(array[i]+array[j]==tsum):
#                 res.append(array[i])
#                 res.append(array[j])
#                 break
#             while i<j and array[i]+array[j]>tsum:
#                 j = j-1
#             while i<j and array[i]+array[j]<tsum:
#                 i += 1
#         return res
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        for i in array:
            if tsum-i in array:
                if tsum-i==i:
                    if array.count(i)>1:
                        return [i,i]
                else:
                    return [i,tsum-i]
        return []