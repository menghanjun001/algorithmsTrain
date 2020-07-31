# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res=[]
        self.dfs(root,res)
        res=sorted(list(set(res)))
        if len(res)==1:
            return -1
        return res[-2]

    def dfs(self, root, res):
        if not root:
            return
        res.append(root.val)
        self.dfs(root.left,res)
        self.dfs(root.right,res)