# -*- coding:utf-8 -*-
class Solution:
    @classmethod
    def FindNumbersWithSum(cls, array, tsum):
        #这里if len(array)<0 是错的，当为[]时left，right无法赋值
        #鲁棒性
        if len(array)<=0 or tsum<0:
            return []
        left=0
        right=len(array)-1
        while True:
            if array[left]+array[right]>tsum:
                right-=1
            elif array[left]+array[right]<tsum:
                left+=1
            elif array[left]+array[right]==tsum:
                return array[left],array[right]
            #鲁棒性
            if left==right:
                return []
s=Solution.FindNumbersWithSum([1,2,4,7,11,16],10)
print(s)



