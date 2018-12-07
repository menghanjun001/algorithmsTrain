# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        maxIndex=nums.index(max(nums))
        root=TreeNode(max(nums))
        root.left=self.constructMaximumBinaryTree(nums[:maxIndex])
        root.right=self.constructMaximumBinaryTree(nums[maxIndex+1:])
        return root