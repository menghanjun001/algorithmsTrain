# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        self.matrix=matrix
        a=[]
        while matrix:
            # print('丢弃前',matrix)
            a.extend(matrix.pop(0))
            # print('丢弃后',matrix)
            matrix=self.clockwise(matrix)
            # print('旋转后',matrix)
        return a
    def clockwise(self,a):
        b=[list(row) for row in list(zip(*a))[::-1]]
        return b
# a=[[1,2],
#    [3,4]]
# x=Solution()
# print(x.printMatrix(a))