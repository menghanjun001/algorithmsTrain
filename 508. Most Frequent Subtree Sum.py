# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import Counter


class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res=[]
        ans=[]
        self.sumOfSubtree(root,res)
        # print(res)
        d=Counter(res)
        # print(d)
        ma=max([val for val in d.values()])
        # print(ma)
        for key in d:
            if d[key]==ma:
                ans.append(key)
        return ans

    def sumOfSubtree(self, root, res):
        if not root:
            return 0
        lsum=self.sumOfSubtree(root.left,res)
        rsum=self.sumOfSubtree(root.right,res)
        res.append(lsum+root.val+rsum)
        return lsum+root.val+rsum