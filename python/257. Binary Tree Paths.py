# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res=[]
        self.dfs(root,[],res)
        return res

    def dfs(self, root, temp, res):
        if not root:
            return
        # else:
        #     print(root.val)
        temp.append(str(root.val))
        if not root.left and not root.right:
            res.append('->'.join(temp))
        if root.left:
            self.dfs(root.left, temp, res)
        if root.right:
            self.dfs(root.right, temp, res)
        temp.pop()