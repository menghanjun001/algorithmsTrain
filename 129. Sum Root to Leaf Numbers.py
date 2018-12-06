# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left and not root.right:
            return root.val

        res=[]
        self.dfs(root,'',res)
        return sum(res)
    def dfs(self,root,temp,res):
        if not root:
            return
        if not root.left and not root.right:
            temp+=str(root.val)
            res.append(int(temp))
        self.dfs(root.left,temp+str(root.val),res)
        self.dfs(root.right,temp+str(root.val),res)
