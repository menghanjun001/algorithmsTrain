# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
        node=head
        length=0
        while node.next:
            length+=1
            node=node.next
        length+=1
        k=k%length #取模

        if k==0:
            return head #原地不动

        # node.next=head
        left=right=head
        for i in range(k):
            right=right.next
        while right.next:
            left=left.next
            right=right.next
        temp=left.next
        left.next=None
        right.next=head
        head=temp
        return head
