# -*- coding:utf-8 -*-
class Solution:
    @classmethod
    def FindGreatestSumOfSubArray(cls, array):
        # write code here
        max=array[0]
        tmp=array[0]
        for i in range(1,len(array)):
            if tmp<=0:
                tmp=array[i]
            else:
                tmp+=array[i]
            if max<tmp:
                max=tmp
        return max
s=Solution.FindGreatestSumOfSubArray([-2,-8,-1,-5,-9])
print(s)
