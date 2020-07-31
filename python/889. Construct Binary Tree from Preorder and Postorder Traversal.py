# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        # print(pre)
        # print(post)
        if not pre or not post:
            return None

        root=TreeNode(pre[0])
        if len(pre)==1:
            return root
        preIndex=pre.index(post[-2])
        # postIndex=post.index(pre[1])
        root.left=self.constructFromPrePost(pre[1:preIndex],post[:preIndex-1])
        root.right=self.constructFromPrePost(pre[preIndex:],post[preIndex-1:-1])
        return root