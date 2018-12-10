# definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: dt[int]
        """
        d={}
        self.inOrder(root, d)
        maxCount=0
        for i in d:
            maxCount=max(d[i],maxCount)
        return [key for key in d if d[key]==maxCount]
    def inOrder(self, root, d):
        if not root:
            return None
        self.inOrder(root.left, d)
        if root.val not in d:
            d[root.val]=1
        else:
            d[root.val]+=1
        self.inOrder(root.right, d)
if __name__ == '__main__':
    a=TreeNode(2)
    b=TreeNode(1)
    c=TreeNode(3)
    a.left=b
    a.right=c
    c.right=TreeNode(2)
    cc=Solution()
    print(cc.findMode(a))