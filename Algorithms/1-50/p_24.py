# Swap Nodes in Pairs
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        first = None
        r = ListNode(None)
        cur_r = r
        cur = head
        while cur is not None:
            if first is None:
                first = cur
                cur = cur.next
            else:
                cur_r.next = cur
                first.next = cur.next
                cur.next = first
                cur_r = first
                cur = first.next
                first = None
        if first is not None:
            cur_r.next = first
        return r.next