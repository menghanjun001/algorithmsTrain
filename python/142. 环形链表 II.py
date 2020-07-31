# # Definition for singly-linked list.
# # class ListNode(object):
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None
#
# class Solution(object):
#     def detectCycle(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         if not head:
#             return None
#         lis=[]
#         slow=fast=head
#         while fast.next and fast.next.next:
#             if slow in lis:
#                 return slow
#             lis.append(slow)
#             #不添加值直接比较指针也可以
#             slow=slow.next
#             fast=fast.next.next
#             # lis.append(slow.val)
#
#         return None

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return None
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast=fast.next.next
            if slow==fast:
                break
        if slow!=fast:
            return None
        slow=head
        while slow!=fast:
            slow=slow.next
            fast=fast.next
        return slow