# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # write code here
        if not root:
            return None
        currentStack = [root]
        # nextStack=[]
        res=[]
        while currentStack:
            nextStack = []
            val=[]
            for i in currentStack:
                if i.left:
                    nextStack.append(i.left)
                if i.right:
                    nextStack.append(i.right)
                val.append(i.val)
            res.append(val)
            currentStack = nextStack
        return (res.pop()).pop(0)