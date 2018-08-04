# -*- coding:utf-8 -*-
class Solution:
    @classmethod
    def jumpFloor(cls, number):
        f=[]
        f.append(0)
        f.append(1)
        f.append(2)
        for i in range(3,number+1):
            f.append(f[i-1]+f[i-2])
        return f[number]

# print(Solution.jumpFloor(2))