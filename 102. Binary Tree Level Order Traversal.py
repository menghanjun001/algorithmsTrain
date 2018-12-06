# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res=[[root.val]]
        currentStack=[root]
        while currentStack:
            nextStack=[]
            value=[]
            for node in currentStack:
                if node.left:
                    nextStack.append(node.left)
                    value.append(node.left.val)
                if node.right:
                    nextStack.append(node.right)
                    value.append(node.right.val)
            if value:
                res.append(value)
            currentStack=nextStack
        return res