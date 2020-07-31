# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    @classmethod
    def duplicate(cls, numbers, duplication):
        # write code here
        d={}
        for i in range(len(numbers)):
            if numbers[i] not in d:
                d[numbers[i]]=1
            else:
                duplication.append(numbers[i])
                return True,duplication
            if i==len(numbers)-1 and duplication ==[]:
                return False,duplication
# s=Solution.duplicate([2,1,3,1,4],[])
# print(s)