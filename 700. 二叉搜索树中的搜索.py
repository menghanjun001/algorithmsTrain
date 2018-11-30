# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return None
        if root.val==val:
            return root
        elif root.val>val:
            return self.searchBST(root.left,val) #为什么一定要return?递归一定要有return吗
        else:
            return self.searchBST(root.right,val)