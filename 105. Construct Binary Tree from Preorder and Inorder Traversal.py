# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None
        root=TreeNode(preorder.pop(0))
        rootIndex=inorder.index(root.val)
        root.left=self.buildTree(preorder,inorder[:rootIndex])
        root.right=self.buildTree(preorder,inorder[rootIndex+1:])
        return root