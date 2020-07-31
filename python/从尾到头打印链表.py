# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        result=[]
        if listNode is None:
            return result
        else:
            while listNode.next:
                result.extend([listNode.val])       #添加当前指针指向的值
                listNode=listNode.next    #next指针指向下个结点
            result.extend([listNode.val]) #添加最后一个结点没有下个指针了，不满足循环
        return result[::-1]