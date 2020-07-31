# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        list1=[]
        list2=[]
        self.getList(root1,list1)
        self.getList(root2,list2)
        if list1==list2:
            return True
        else:
            return False

    def getList(self,root,list):
        if not root:
            return 
        if not root.left and not root.right:
            list.append(root.val)
        self.getList(root.left,list)
        self.getList(root.right,list)
        return