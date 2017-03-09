# Remove Nth Node From End of List
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        l_len = 1
        cur = head
        while cur.next is not None:
            l_len += 1
            cur = cur.next
        m = l_len - n
        if m == 0:
            return head.next
        else:
            cur = head
            i = 1
            while i < m:
                cur = cur.next
                i += 1
            if cur.next is not None:
                cur.next = cur.next.next
            return head