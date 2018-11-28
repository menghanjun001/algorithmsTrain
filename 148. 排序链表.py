# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: #not 'if not head: return None'
            return head
        middle=self.getMiddle(head)
        lHead=head
        rHead=middle.next
        middle.next=None
        return self.merge(self.sortList(lHead),self.sortList(rHead))

    def getMiddle(self, head):
        if not head:
            return None
        slow=fast=head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        return slow

    def merge(self,lHead,rHead):
        myNode=ListNode(0)
        head=myNode
        i=lHead
        j=rHead
        while i and j:
            if i.val <= j.val:
                myNode.next=i
                i=i.next
            else:
                myNode.next=j
                j=j.next
            myNode=myNode.next
        if i:
            myNode.next=i
        if j:
            myNode.next=j

        return head.next


