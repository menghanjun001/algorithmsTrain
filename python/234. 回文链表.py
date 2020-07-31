# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        slow=fast=head
        stack=[]
        while fast and fast.next:
            stack.append(slow)
            slow=slow.next
            fast=fast.next.next
        if not fast: # 偶数
            slow=slow
        else:        # 奇数
            slow=slow.next
        for i in stack[::-1]:
            if i.val!=slow.val:
                return False
            slow=slow.next
        return True