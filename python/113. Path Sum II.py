# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, su):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res=[]
        ress=[]
        self.dfs(root,[],res)
        for i in res:
            if sum(i)==su:
                ress.append(i)
        return ress

    def dfs(self,root,temp,res):
        if not root:
            return
        if not root.left and not root.right:
            temp+=[root.val]
            res.append(temp)
            return
        self.dfs(root.left,temp+[root.val],res)
        self.dfs(root.right,temp+[root.val],res)