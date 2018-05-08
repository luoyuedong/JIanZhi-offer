__author__ = 'luoyuedong'
__date__ = '2018/5/5 13:36'

# -*- coding:utf-8 -*-
class Solution:
    # 返回对应char
    dict={}
    l=""
    def FirstAppearingOnce(self):
        for x in self.l:
            if self.dict[x]==1:
                return x
        return '#'
    def Insert(self, char):
        self.l=self.l+char
        if self.dict.has_key(char):
            self.dict[char]+=1
        else:
            self.dict[char]=1