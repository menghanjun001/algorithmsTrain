# -*- coding:utf-8 -*-
class Solution:
    @classmethod
    def multiply(cls, A):
        # write code here
        if not A:
            return []
        shang=[1]
        xia=[1]
        B=[]
        for i in range(1,len(A)):
            xia.append(xia[i-1]*A[i-1])
            shang.append(shang[i-1]*A[-i])
        for i in range(len(A)):
            B.append(shang[-i-1]*xia[i])
        return B
# a=Solution.multiply([1,2,3,4,5])
