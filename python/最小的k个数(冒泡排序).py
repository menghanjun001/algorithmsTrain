# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        def bubbleSort(l):
            for i in range(len(l)):
                for j in range(1,len(l)-i):
                    if l[j-1]>l[j]:
                        l[j-1],l[j]=l[j],l[j-1]
            return l
        if not tinput or k>len(tinput):
            return []
        else:
            return bubbleSort(tinput)[:k]
