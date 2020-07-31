# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        res=[]
        self.postOrder(root,res)
        return sum(res)

    def postOrder(self, root,res):
        if not root:
            return 0
        lsum=self.postOrder(root.left,res)
        rsum=self.postOrder(root.right,res)
        res.append(abs(lsum-rsum))
        return lsum+root.val+rsum
