# -*- coding:utf-8 -*-
class Solution:
    @classmethod
    def GetLeastNumbers_Solution(cls, tinput, k):
        # write code here
        def quickSort(l):
            if not l:
                return []
            pivot=l[0]
            left=quickSort([i for i in l[1:] if i<pivot])
            right=quickSort([i for i in l[1:] if i>=pivot])
            return left+[pivot]+right
        if not tinput or k>len(tinput):
            return []
        else:
            return quickSort(tinput)[:k]

# s=Solution.GetLeastNumbers_Solution([4,5,1,6,2,7,3,8],10)
# print(s)