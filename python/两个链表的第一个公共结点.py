# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if not pHead1 or not pHead2:
            return None
        list=[]
        while pHead1:
            list.append(pHead1.val)
            pHead1=pHead1.next
        while pHead2:
            if pHead2.val in list:
                return pHead2
            else:
                pHead2=pHead2.next