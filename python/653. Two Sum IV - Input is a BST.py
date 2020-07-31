# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        res=[]
        self.dfs(root,res)
        res.sort()
        left=0
        right=len(res)-1
        while left<right:
            print(left,res[left],right,res[right])
            if res[left]+res[right]<k:
                left+=1
            elif res[left]+res[right]>k:
                right-=1
            else:
                return True
        return False
    def dfs(self, root, res):
        if not root:
            return
        res+=[root.val]
        if not root.left and not root.right:
            return
        self.dfs(root.left,res)
        self.dfs(root.right,res)