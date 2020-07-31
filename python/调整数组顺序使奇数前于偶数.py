# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        from collections import deque
        left=0
        right=len(array)-1
        res=deque()
        for i in range(len(array)):
            if array[right]&1==1:
                res.appendleft(array[right])
            if array[left]&1==0:
                res.append(array[left])
            left+=1
            right-=1
        return res
# from collections import deque
# array=[1,2,3,4,5,6,7]
# left=0
# right=len(array)-1
# res=deque()
# for i in range(len(array)):
#     if array[right]&1==1:
#         res.appendleft(array[right])
#     if array[left]&1==0:
#         res.append(array[left])
#     left+=1
#     right-=1
# print(list(res))