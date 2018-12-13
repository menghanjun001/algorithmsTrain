# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        res=[]
        while head.next:
            res.append(head.val)
            head=head.next
        res.append(head.val)
        return self.Construct(res)

    def Construct(self, res):
        if not res:
            return None
        mid=len(res)//2
        root=TreeNode(res[mid])
        root.left=self.Construct(res[:mid])
        root.right=self.Construct(res[mid+1:])
        return root
