# # Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        res = self.inorder(root)
        node=TreeNode(res[0])
        head=node
        for i in range(1,len(res)):
            node.left=None
            node.right=TreeNode(res[i])
            node=node.right
        return head

    def inorder(self, root):
        if not root:
            return []
        res = []
        res += self.inorder(root.left)
        res += [root.val]
        res += self.inorder(root.right)
        return res

# class Solution(object):
#     def increasingBST(self, root, tail=None):
#         """
#         :type root: TreeNode
#         :rtype: TreeNode
#         """
#
#         if not root:
#             return tail
#
#         res = self.increasingBST(root.left, root)
#         root.left = None
#         root.right = self.increasingBST(root.right, tail)
#
#         return res