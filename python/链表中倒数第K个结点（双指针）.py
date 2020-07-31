# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        if not head or k<1:
            return None
        p1=head
        p2=head
        for i in range(k-1):
            if p2.next:
                p2=p2.next
            else:
                return None
        while True:
            if p2.next:
                p1=p1.next
                p2=p2.next
            else:  #不加else就错了
                return p1