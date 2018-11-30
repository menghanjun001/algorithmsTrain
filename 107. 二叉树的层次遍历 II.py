# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ans=[]
        currentStack=[root]
        while currentStack:
            nextStack=[]
            nodeVal=[]
            for i in currentStack:
                if i.left:
                    nextStack.append(i.left)
                if i.right:
                    nextStack.append(i.right)
                nodeVal.append(i.val)
            currentStack=nextStack
            ans.append(nodeVal)
        return ans[::-1]
