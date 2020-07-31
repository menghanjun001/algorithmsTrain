# -*- coding:utf-8 -*-
class Solution:
    @classmethod
    def minNumberInRotateArray(cls, rotateArray):
        # write code here
        if len(rotateArray)==0:
            return 0
        if len(rotateArray)==1:
            return rotateArray[0]
        left=0
        right=len(rotateArray)-1

        while True:
            if right==left+1:
                return rotateArray[right]
            else:
                pivot=(left+right)//2
                if rotateArray[pivot]>=rotateArray[left]:
                    left=pivot
                elif rotateArray[pivot]<=rotateArray[right]:
                    right=pivot
s=Solution.minNumberInRotateArray([1])
print(s)
