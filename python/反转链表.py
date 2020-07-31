# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     # 返回ListNode
#     def ReverseList(self, pHead):
#         try:
#             # write code here
#             p = pHead
#             q = ListNode(p.val)
#             if pHead is None:
#                 return None
#             while p.next:
#                 p = p.next
#                 t = ListNode(p.val)
#                 t.next = q
#                 q = t
#             return q   #为什么return q？ p作为反转后的头指针不是应该指向整个链表吗？
#         except BaseException:
#             return None

class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        last=None
        if not pHead:
            return None
        while pHead.next:
            tmp=pHead.next
            pHead.next=last
            last=pHead
            pHead=tmp
        pHead.next=last
        return pHead


