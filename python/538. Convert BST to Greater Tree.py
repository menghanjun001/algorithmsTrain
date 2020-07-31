# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        su=[0]
        self.postOrder(root,su)
        return root

    def postOrder(self, root, su):
        if not root:
            return None
        self.postOrder(root.right,su)
        root.val+=su[-1]
        su.append(root.val)
        self.postOrder(root.left,su)