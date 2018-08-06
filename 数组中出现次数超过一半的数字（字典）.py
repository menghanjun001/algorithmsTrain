# -*- coding:utf-8 -*-
class Solution:
    @classmethod
    def MoreThanHalfNum_Solution(cls, numbers):
        # write code here
        d={}
        for i in range(len(numbers)):
            if numbers[i] not in d:
                d[numbers[i]]=1
            else:
                d[numbers[i]]+=1
            if d[numbers[i]]>len(numbers)//2:
                # print('d[numbers[i]]>=len(numbers)/2')
                # print(numbers[i],d[numbers[i]],len(numbers)/2)
                # print('over')
                return numbers[i]
            # print(i,len(numbers),numbers[i],d[numbers[i]])
            if i == len(numbers)-1:
                # print('meizhaodao')
                return 0

s=Solution.MoreThanHalfNum_Solution([1,2,3,2,4,2,5,2,3])
print(s)



