__author__ = 'luoyuedong'
__date__ = '2018/4/17 23:00'


def replaceSpace(s):
    s = s.replace(' ', '%20')
    return s

a = replaceSpace('Hello world')
print(a)