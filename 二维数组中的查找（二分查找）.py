# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if not target or array==[[]]:
            return False
        i=0
        j=len(array[0])-1
        while True:
            if target>array[i][j] and i<len(array)-1:
                i+=1
            elif target<array[i][j] and j>0:
                j-=1
            elif target==array[i][j]:
                return True
            else:
                return False