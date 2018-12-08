# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res=[]
        ress=[]
        self.dfs(root,res)
        res.sort()
        for i in range(1,len(res)):
            ress.append(abs(res[i]-res[i-1]))
        return min(ress)

    def dfs(self, root, res):
        res+=[root.val]
        if not root.left and not root.right:
            return
        if root.left:
            self.dfs(root.left,res)
        if root.right:
            self.dfs(root.right,res)