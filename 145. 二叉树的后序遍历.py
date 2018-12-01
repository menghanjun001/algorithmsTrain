# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res=[]
        res+=self.postorderTraversal(root.left)
        res+=self.postorderTraversal(root.right)
        res+=[root.val]
        return res