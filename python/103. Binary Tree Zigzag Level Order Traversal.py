# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res=[[root.val]]
        currentStack=[root]
        flag=True  #False为从右到左
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
                if flag:
                    res.append(value[::-1])

                else:
                    res.append(value)
                flag ^= True
            currentStack=nextStack
        return res