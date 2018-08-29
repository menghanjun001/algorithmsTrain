# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.data=[]
    def Insert(self, num):
        # write code here
        # if len(self.data)==0:
        #     self.data.append(num)
        # elif len(self.data)==1:
        #     if num>self.data[0]:
        #         self.data.append(num)
        #     else:
        #         self.data.insert(0,num)
        # else:
        #     for i in range(1,len(self.data)):
        #         if self.data[i-1]<=num<=self.data[i]:
        #             self.data.insert(i,num)
        #             break
        self.data.append(num)
        self.data.sort()
    def GetMedian(self,data):
        # write code here
        l=len(self.data)
        if l%2==0:
            return (self.data[l/2]+self.data[l/2-1])/2.0
        else:
            return self.data[l//2]