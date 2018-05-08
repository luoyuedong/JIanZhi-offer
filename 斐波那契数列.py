__author__ = 'luoyuedong'
__date__ = '2018/4/19 9:56'


class Solution:
    def Fibonacci(self, n):
        a=0
        b=1
        while(n):
            b = a+b
            a = b-a
            n -= 1
        return a