# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        lst=[2**i*3**j*5**k for i in range(30) for j in range(25) for k in range(20)]
        lst.sort()
        if index==0:
            return 0
        else:
            return lst[index-1]
