# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        currentStack=[root]
        val=[]
        while currentStack:
            nextStack=[]
            sum=0
            for i in currentStack:
                if i.left:
                    nextStack.append(i.left)
                if i.right:
                    nextStack.append(i.right)
                sum+=i.val
            val.append(sum/len(currentStack))
            currentStack=nextStack
        return val