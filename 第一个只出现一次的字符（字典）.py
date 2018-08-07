# -*- coding:utf-8 -*-
class Solution:
    @classmethod
    def FirstNotRepeatingChar(cls, s):
        # write code here
        d={}
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i,j in d.items():
            if j==1:
                print(s.find(i))
                # return s.find(i)
                break
            # else:
            #     return -1
Solution.FirstNotRepeatingChar('google')
