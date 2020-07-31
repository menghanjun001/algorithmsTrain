# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        d={}
        for i in range(1,n+1):
            d[i]=str(i).count('1')
        return sum(d.values())
