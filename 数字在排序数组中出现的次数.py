# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        return self.biS(data,k+0.5)-self.biS(data,k-0.5)
    def biS(self,data,num):
        start=0
        end=len(data)-1
        while start<=end:
            mid=(end-start)/2+start
            if data[mid]<num:
                start=mid+1
            elif data[mid]>num:
                end=mid-1
        return start