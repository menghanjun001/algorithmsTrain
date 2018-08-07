# -*- coding:utf-8 -*-
class Solution:
    @classmethod
    def FindContinuousSequence(cls, tsum):
        # write code here
        if tsum<=0:
            return []
        s=[i for i in range(tsum)]
        ss=[]
        left=0
        right=0
        while True:
            if sum(s[left:right+1])>tsum:
                # print('s[left]=%s,sum=%s' % (s[left], s[left:right + 1]))
                left+=1

            elif sum(s[left:right+1])<tsum:
                # print('s[right]=%s,sum=%s'%(s[right],s[left:right+1]))
                right+=1

            else:
                ss.append(s[left:right+1])
                # print(ss)
                right+=1
            if left==len(s)-1 and right==len(s)-1:
                return ss

s=Solution.FindContinuousSequence(9)
print(s)
