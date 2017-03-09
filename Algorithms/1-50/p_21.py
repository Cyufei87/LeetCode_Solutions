# Merge Two Sorted Lists
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_cur = l1
        l2_cur = l2
        r = ListNode(None)
        r_cur = r
        while l1_cur is not None and l2_cur is not None:
            if l1_cur.val <= l2_cur.val:
                r_cur.next = l1_cur
                l1_cur = l1_cur.next
                r_cur = r_cur.next
            else:
                r_cur.next = l2_cur
                l2_cur = l2_cur.next
                r_cur = r_cur.next
        if l1_cur is None:
            r_cur.next = l2_cur
        else:
            r_cur.next = l1_cur
        return r.next
