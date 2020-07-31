# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        res = []
        self.dfs(t, res)
        return ''.join(res)

    def dfs(self, t, res):
        if not t:
            return
        res += [str(t.val)]
        if not t.left and not t.right:
            return

        if t.left:
            res += ['(']
            self.dfs(t.left, res)
            res += [')']
        else:
            res += ['(']

            res += [')']
        if t.right:
            res += ['(']
            self.dfs(t.right, res)
            res += [')']