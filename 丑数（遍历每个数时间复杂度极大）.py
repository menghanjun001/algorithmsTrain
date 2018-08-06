# -*- coding:utf-8 -*-
class Solution:
    @classmethod
    def GetUglyNumber_Solution(cls, index):
        # write code here
        count=0
        def isUglyNumber(x):
            for i in [2,3,5]:
                while x%i==0:
                    x/=i
            if x==1:
                return True
            else:
                return False
        for i in range(1,10000):
            if isUglyNumber(i):
                # print(i)
                count+=1
            if count==index:
                return i
# s={}
# for i in range(1,500):
#     s[i]=Solution.GetUglyNumber_Solution(i)
# print(s)