# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        listNode=[]
        if pHead.next:
            while True:
                if pHead not in listNode:
                    listNode.append(pHead)
                else:
                    return pHead
                pHead=pHead.next
        else:
            return None