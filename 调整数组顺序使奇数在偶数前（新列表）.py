# -*- coding:utf-8 -*-

class Solution:
    @classmethod
    def reOrderArray(cls, array):
        # write code here
        d=[]
        for i in array:
            if i%2!=0:
                d.append(i)
        for i in array:
            if i%2==0:
                d.append(i)
        return d
array=[1,2,3,4,5]
print(Solution.reOrderArray(array))

