# -*- coding:utf-8 -*-
class Solution:
    @classmethod
    def maxInWindows(cls, num, size):
        # write code here
        if size==0:
            return []
        m=[]
        for i in range(len(num)-size+1):
            m.append(max(num[i:i+size]))
        return m
# print(Solution.maxInWindows([2,3,4,2,6,2,5,1],3))