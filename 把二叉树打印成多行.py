# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        from collections import deque
        if not pRoot:
            return []
        currentStack=[pRoot]
        list=[]
        while currentStack:
            nextStack=[]
            val = []
            for i in currentStack:
                if i.left:
                    nextStack.append(i.left)
                if i.right:
                    nextStack.append(i.right)
                val.append(i.val)
            list.append(val)
            currentStack=nextStack
        return list


