# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if not root:
            return None #return None 和 return 都可以
        if root.val>R:
            return self.trimBST(root.left,L,R)
        if root.val<L:
            return self.trimBST(root.right,L,R)
        root.left=self.trimBST(root.left,L,R)
        root.right=self.trimBST(root.right,L,R)
        return root
