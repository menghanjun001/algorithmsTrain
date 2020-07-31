# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        if not pNode:
            return None
        if pNode.right:
            res=pNode.right
            while res.left:
                res=res.left
            return res
        # else:   是错误的 没判断是否有父节点
        while pNode.next:
            tmp=pNode.next
            while tmp.left==pNode:
                return tmp
            pNode=tmp