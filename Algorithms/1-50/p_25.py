# Reverse Nodes in k-Group
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        def reverse(l, first=None):
            cur = l
            new_l = first
            while cur is not None:
                n = cur.next
                cur.next = new_l
                new_l = cur
                cur = n
            return new_l
        cur = head
        cur_i = 0
        r = ListNode(None)
        r_cur = r
        while cur is not None:
            if cur_i == 0:
                k_f = cur
            cur_i += 1
            if cur_i == k:
                n = cur.next
                cur.next = None
                r_l = reverse(k_f)
                r_cur.next = r_l
                r_cur = k_f
                cur_i = 0
                cur = n
            else:
                cur = cur.next
        if cur_i > 0:
            r_cur.next = k_f
        return r.next