__author__ = 'luoyuedong'
__date__ = '2018/5/5 21:18'




def merg_sort(a,b):
    c = []
    while a and b:
        if a[0]>=b[0]:
            c.append(b.pop(0))
        else:
            c.append(a.pop(0))
    while a:
        c.append(a.pop(0))
    while b:
        c.append(b.pop(0))
    return c
