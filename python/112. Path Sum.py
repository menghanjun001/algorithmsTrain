# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, su):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        res=[]
        self.dfs(root,[],res)
        for each in res:
            if sum(each) == su:
                return True
        return False

    def dfs(self,root,temp,res):
        if not root:
            return
        if not root.left and not root.right:
            temp+=[root.val]
            res.append(temp)
            return
        self.dfs(root.left,temp+[root.val],res)
        self.dfs(root.right,temp+[root.val],res)

