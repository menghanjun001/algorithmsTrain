# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        currentStack=[root]
        # nextStack=[]
        val=[]
        while currentStack:
            nextStack=[]
            for i in currentStack:
                if i.left:
                    nextStack.append(i.left)
                if i.right:
                    nextStack.append(i.right)
                val.append(i.val)
            currentStack=nextStack
        return val