# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import copy


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        a,b=headA,headB
        aLen=0
        bLen=0
        while a:
            aLen+=1
            a=a.next
        while b:
            bLen+=1
            b=b.next
        if aLen>bLen:
            for i in range(aLen-bLen):
                headA=headA.next
        elif bLen>aLen:
            for i in range(bLen-aLen):
                headB=headB.next
        while headA:
            if headA==headB:
                return headA
            else:
                headA=headA.next
                headB=headB.next
        return None