# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        currentStack=[root]
        res=[root.val]
        while currentStack:
            nextStack=[]
            value=[]
            for i in currentStack:
                if i.left:
                    nextStack.append(i.left)
                    value.append(i.left.val)
                if i.right:
                    nextStack.append(i.right)
                    value.append(i.right.val)
            if value:
                res.append(min(value))
            currentStack=nextStack
        return res