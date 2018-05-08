__author__ = 'luoyuedong'
__date__ = '2018/4/19 11:20'


def reOrderArray(array):
    res = []
    for i in range(len(array)):
        if(array[i]%2==1):
            res.append(array[i])
    for i in range(len(array)):
        if(array[i]%2==0):
            res.append(array[i])
    return res

def reOrderArray2(array):
    return sorted(array,key=lambda c:c%2,reverse=True)
