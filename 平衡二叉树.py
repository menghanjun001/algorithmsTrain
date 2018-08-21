# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if not pRoot:
            return True
        if abs(self.depth(pRoot.left)-self.depth(pRoot.right))>1:
            return False
        # else:
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)
    def depth(self,pRoot):
        if not pRoot:
            return 0
        return max(self.depth(pRoot.left),self.depth(pRoot.right))+1
