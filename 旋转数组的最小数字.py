__author__ = 'luoyuedong'
__date__ = '2018/4/19 9:19'


# -*- coding:utf-8 -*-
class Solution:

    def minOrder(self, rotateArray,left,right):
        minx = rotateArray[left]
        for i in range(len(rotateArray)):
            if rotateArray[i]<minx:
                minx = rotateArray[i]
        return minx

    def minNumberInRotateArray(self, rotateArray):
        if(len(rotateArray)==0):
            return 0
        left = 0
        right = len(rotateArray)-1
        mid = 0
        while(rotateArray[left]>=rotateArray[right]):
            if(right-left==1):
                return rotateArray[right]
            mid = left+(right-left)/2
            if(rotateArray[left]==rotateArray[right] and rotateArray[left]==rotateArray[mid]):
                return self.minOrder(rotateArray,left,right)
            if(rotateArray[left]<=rotateArray[mid]):
                left = mid
            else:
                right = mid



